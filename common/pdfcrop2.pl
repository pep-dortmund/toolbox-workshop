eval '(exit $?0)' && eval 'exec perl -S $0 ${1+"$@"}' && eval 'exec perl -S $0 $argv:q'
  if 0;
use strict;
$^W=1; # turn warning on
#
# pdfcrop.pl
#
# Copyright (C) 2002, 2004 Heiko Oberdiek.
#
# This program may be distributed and/or modified under the
# conditions of the LaTeX Project Public License, either version 1.2
# of this license or (at your option) any later version.
# The latest version of this license is in
#   http://www.latex-project.org/lppl.txt
# and version 1.2 or later is part of all distributions of LaTeX
# version 1999/12/01 or later.
#
# See file "readme.txt" for a list of files that belong to this project.
#
# This file "pdfcrop.pl" may be renamed to "pdfcrop"
# for installation purposes.
#
my $file        = "pdfcrop.pl";
my $program     = uc($&) if $file =~ /^\w+/;
my $version     = "1.5";
my $date        = "2004/06/24";
my $author      = "Heiko Oberdiek";
my $copyright   = "Copyright (c) 2002, 2004 by $author.";

my $patchver 	= "0.4";
my $patchdate	= "2007/02/18";
my $patchauthor = "Piotr Adacha";
my $patchcopy	= "Copyright (c) 2007 by $patchauthor.";
#
# Reqirements: Perl5, Ghostscript
# History:
#   2002/10/30 v1.0: First release.
#   2002/10/30 v1.1: Option --hires added.
#   2002/11/04 v1.2: "nul" instead of "/dev/null" for windows.
#   2002/11/23 v1.3: Use of File::Spec module's "devnull" call.
#   2002/11/29 v1.4: Option --papersize added.
#   2004/06/24 v1.5: Clear map file entries so that pdfTeX
#                    does not touch the fonts.
#

### program identification
my $title = "$program $version, $date - $copyright\n";
$title .= "Patch $patchver, $patchdate - $patchcopy\n";
### error strings
my $Error = "!!! Error:"; # error prefix

### string constants for Ghostscript run
# get Ghostscript command name
my $GS = "gs";
$GS = "gs386"    if $^O =~ /dos/i;
$GS = "gsos2"    if $^O =~ /os2/i;
$GS = "gswin32c" if $^O =~ /mswin32/i;
$GS = "gswin32c" if $^O =~ /cygwin/i;

# Windows detection (no SIGHUP)
my $Win = 0;
$Win = 1 if $^O =~ /mswin32/i;
$Win = 1 if $^O =~ /cygwin/i;

# "null" device
use File::Spec::Functions qw(devnull);
my $null = devnull();

### variables
my $inputfile   = "";
my $outputfile  = "";
my $tmp = "tmp-\L$program\E-$$";
my $confirm_flag = 0;
my $auto_flag = 0;
my @exclude;
my @exclude_auto;
my @pages;
my $stdevp_range = 3;
### option variables
my @bool = ("false", "true");
my %unit = ( 'pt'=>1, 'in'=>0.0138, 'mm'=>0.3527, 'cm' =>0.03527, 'P'=>0.08333333 );
$::opt_help       = 0;
$::opt_debug      = 0;
$::opt_verbose    = 0;
$::opt_gscmd      = $GS;
$::opt_pdftexcmd  = "pdftex";
$::opt_pdfinfocmd = "pdfinfo";
$::opt_margins    = "0 0 0 0";
$::opt_clip       = 0;
$::opt_hires      = 0;
$::opt_papersize  = "";
$::opt_unit = "pt";
$::opt_mode = "standard";
$::opt_exclude = "";
$::opt_sens = 3;
$::opt_align = "lt";

my $usage = <<"END_OF_USAGE";
${title}Syntax:   \L$program\E [options] <input[.pdf]> [output file]
Function: Margins are calculated and removed for each page in the file.
Options:                                                    (defaults:)
  --help              print usage
  --(no)verbose       verbose printing                      ($bool[$::opt_verbose])
  --(no)debug         debug informations                    ($bool[$::opt_debug])
  --gscmd <name>      call of ghostscript                   ($::opt_gscmd)
  --pdftexcmd <name>  call of pdfTeX                        ($::opt_pdftexcmd)
  --pdfinfocmd <name> call of pdfinfo			    ($::opt_pdfinfocmd)
  --margins "<left> <top> <right> <bottom>"                 ($::opt_margins)
                      add extra margins, unit is bp. If only one number is
                      given, then it is used for all margins, in the case
                      of two numbers they are also used for right and bottom.
  --(no)clip          clipping support, if margins are set, ignored when
		      in absolute mode  ($bool[$::opt_clip])
  --(no)hires         using `%%HiResBoundingBox'            ($bool[$::opt_hires])
                      instead of `%%BoundingBox'
  --papersize <foo>   parameter for gs's -sPAPERSIZE=<foo>,
                      use only with older gs versions <7.32 ($::opt_papersize)
  --unit <unitname>   set margins unit (pt, in, mm, cm, P) ($::opt_unit)
  --mode <standard | absolute | auto | auto2> ($::opt_mode)
		      pick crop mode :

		      standard - orginal pdfcrop working mode - each page is cropped
		      to individual size based od bbox size and taking margins into
		      account

		      absolute - clip size will be calculated based on pagesize returned
		      from pdfinfo command, not bbox. Thus, all pages will have
		      same size. Margin option set cropping box (i. e. how much to crop
                      from each side

  	              auto - clip size will be calculated based on maximum bbox dimensions
		      from all pages. Thus, all pages will have same size, 
		      minimum required to fit all document elements 

		      auto2 - clip size will be calculated based on maximum bbox size
		      from all pages. Thus, all pages will have same size, 
		      minimum required to fit all document elements This differs from auto mode
			- while in auto mode output size is stretched to fit all page elements,
  		 	in auto2 mode, bbox is first moved to fit actual elements and then
		      resized, if required. This should result in bit smaller pages than
		      auto mode.
	
  --exclude "<page1> <page2> ..." 
		      indicates which pages to exclude from calculations in Auto mode. 
		      You can put several page numbers here and as well as words "auto"
		      or "fullauto".
		      Auto causes pdfclip to stastitically choose pages
		      to exclude and ask for confirmation for each, wile fullauto means
		      to confirm all.
  --sens <sensitivity>
		      Sensitivity of auto exclusion. Default value is 3. Lower values
		      exclude more pages larger - less

  --align <lt | lb | rt | rb > ($::opt_align)
		      Used only in auto2 mode, decides to which page corner align page contents. 
		      l - left, t - top , r - rigth, b - bottom
Examples:
  \L$program\E --margins 10 input.pdf output.pdf
  \L$program\E --margins '5 10 5 20' --clip input.pdf output.pdf
  \L$program\E --mode auto input.pdf output.pdf
  \L$program\E --mode auto --exclude fullauto input.pdf output.pdf

END_OF_USAGE

### process options
my @OrgArgv = @ARGV;
use Getopt::Long;
GetOptions(
  "help!",
  "debug!",
  "verbose!",
  "gscmd=s",
  "pdftexcmd=s",
  "pdfinfocmd=s",
  "margins=s",
  "clip!",
  "hires!",
  "papersize=s",
  "unit=s",
  "mode=s",
  "exclude=s",
  "sens=f",
  "align=s",
) or die $usage;
!$::opt_help or die $usage;

$::opt_verbose = 1 if $::opt_debug;

@ARGV >= 1 or die $usage;

print $title;

@ARGV <= 2 or die "$Error Too many files!\n";

### input file
$inputfile = shift @ARGV;

if (! -f $inputfile) {
    if (-f "$inputfile.pdf") {
        $inputfile .= ".pdf";
    }
    else {
        die "$Error Input file `$inputfile' not found!\n";
    }
}

print "* Input file: $inputfile\n" if $::opt_debug;

### output file
if (@ARGV) {
    $outputfile = shift @ARGV;
}
else {
    $outputfile = $inputfile;
    $outputfile =~ s/\.pdf$//i;
    $outputfile .= "-crop.pdf";
}

print "* Output file: $outputfile\n" if $::opt_debug;

### margins
my ($llx, $lly, $urx, $ury) = (0, 0, 0, 0);
if ($::opt_margins =~
        /^\s*([\-\.\d]+)\s+([\-\.\d]+)\s+([\-\.\d]+)\s+([\-\.\d]+)\s*$/) {
    ($llx, $lly, $urx, $ury) = ($1, $2, $3, $4);
}
else {
    if ($::opt_margins =~ /^\s*([\-\.\d]+)\s+([\-\.\d]+)\s*$/) {
        ($llx, $lly, $urx, $ury) = ($1, $2, $1, $2);
    }
    else {
        if ($::opt_margins =~ /^\s*([\-\.\d]+)\s*$/) {
            ($llx, $lly, $urx, $ury) = ($1, $1, $1, $1);
        }
        else {
            die "$Error Parse error (option --margins)!\n";
        }
    }
}

$llx = $llx / $unit{$::opt_unit};
$lly = $lly / $unit{$::opt_unit};
$urx = $urx / $unit{$::opt_unit};
$ury = $ury / $unit{$::opt_unit};

print "* Margins: $llx pt $lly pt $urx pt $ury pt\n" if $::opt_debug;

$stdevp_range = $::opt_sens >= 0 ? $::opt_sens : 3 ;
print "* Sensitivity: $stdevp_range \n" if $::opt_debug;

### cleanup system
my @unlink_files = ();
my $exit_code = 1;
sub clean {
    print "* Cleanup\n" if $::opt_debug;
    if ($::opt_debug) {
        print "* Temporary files: @unlink_files\n";
    }
    else {
        for (; @unlink_files>0; ) {
            unlink shift @unlink_files;
        }
    }
}
sub cleanup {
    clean();
    exit($exit_code);
}
$SIG{'INT'} = \&cleanup;
$SIG{'__DIE__'} = \&clean;

### Calculation of BoundingBoxes

my $cmdpipe="";
my $cmd = "";
if ( lc( $::opt_mode ) eq "absolute" ){
	$cmdpipe = "$::opt_pdfinfocmd $inputfile |";
} else {
	$cmd = "$::opt_gscmd -sDEVICE=bbox -dBATCH -dNOPAUSE ";
	$cmd .= "-sPAPERSIZE=$::opt_papersize " if $::opt_papersize;
	$cmd .= "-c save pop -f " . $inputfile;
	$cmdpipe = $cmd . " 2>&1 1>$null |";
}

my $tmpfile = "$tmp.tex";
push @unlink_files, $tmpfile;
open(TMP, ">$tmpfile") or
    die "$Error Cannot write tmp file `$tmpfile'!\n";
print TMP "\\def\\pdffile{$inputfile}\n";
print TMP <<'END_TMP_HEAD';
\csname pdfmapfile\endcsname{}
\def\page #1 [#2 #3 #4 #5]{%
  \count0=#1\relax
  \setbox0=\hbox{%
    \pdfximage page #1{\pdffile}%
    \pdfrefximage\pdflastximage
  }%
  \pdfhorigin=-#2bp\relax
  \pdfvorigin=#3bp\relax
  \pdfpagewidth=#4bp\relax
  \advance\pdfpagewidth by -#2bp\relax
  \pdfpageheight=#5bp\relax
  \advance\pdfpageheight by -#3bp\relax
  \ht0=\pdfpageheight
  \shipout\box0\relax
}
\def\pageclip #1 [#2 #3 #4 #5][#6 #7 #8 #9]{%
  \count0=#1\relax
  \dimen0=#4bp\relax \advance\dimen0 by -#2bp\relax
  \edef\imagewidth{\the\dimen0}%
  \dimen0=#5bp\relax \advance\dimen0 by -#3bp\relax
  \edef\imageheight{\the\dimen0}%
  \pdfximage page #1{\pdffile}%
  \setbox0=\hbox{%
    \kern -#2bp\relax
    \lower #3bp\hbox{\pdfrefximage\pdflastximage}%
  }%
  \wd0=\imagewidth\relax
  \ht0=\imageheight\relax
  \dp0=0pt\relax
  \pdfhorigin=#6pt\relax
  \pdfvorigin=#7bp\relax
  \pdfpagewidth=\imagewidth
  \advance\pdfpagewidth by #6bp\relax
  \advance\pdfpagewidth by #8bp\relax
  \pdfpageheight=\imageheight\relax
  \advance\pdfpageheight by #7bp\relax
  \advance\pdfpageheight by #9bp\relax
  \pdfxform0\relax
  \shipout\hbox{\pdfrefxform\pdflastxform}%
}%
END_TMP_HEAD

my $page = 0;
if ( lc ( $::opt_mode ) ne "absolute" ) {
print "* Running ghostscript for BoundingBox calculation ...\n"
    if $::opt_verbose;
print "* Ghostscript pipe: $cmdpipe\n" if $::opt_debug;

my $min_llx = 0;
my $min_lly = 0;
my $max_urx = 0;
my $max_ury = 0;

open(CMD, $cmdpipe) or
    die "$Error Cannot call ghostscript!\n";
while (<CMD>) {
    my $bb = ($::opt_hires) ? "%%HiResBoundingBox" : "%%BoundingBox";
    next unless
        /^$bb:\s*([\.\d]+) ([\.\d]+) ([\.\d]+) ([\.\d]+)/o;
    $page++;
    print "* Page $page: $1 $2 $3 $4\n" if $::opt_verbose;
    push(@pages, [ ($1, $2, $3, $4) ]);
    

 if ( lc ($::opt_mode) eq "standard" ) {   
    if ($::opt_clip) {
        print TMP "\\pageclip $page [$1 $2 $3 $4][$llx $lly $urx $ury]\n";
    }
    else {
        my ($a, $b, $c, $d) = ($1 - $llx, $2 - $ury, $3 + $urx, $4 + $lly);
        print TMP "\\page $page [$a $b $c $d]\n";
    }
 }

}

 if ( lc ($::opt_mode) eq "auto" ) { 

 # Handle page exclusion

 my @exclude_string = split ( /[\s,]+/,  $::opt_exclude);

 foreach my $page_word ( @exclude_string ) {
	
	if ( lc($page_word) eq "auto" ) { $auto_flag = 1; next; };
 	if ( lc($page_word) eq "fullauto" ) { $auto_flag=1; $confirm_flag = 1; next;};
	if ( int($page_word) >0 ) { push(@exclude, int($page_word) ); };
	
 }

 # If to perform auto exclusion, do some statistics - average dimensions and stdevp 
 if ( $auto_flag ) {

	print "Auto exclusion enabled \n" if $::opt_debug;
	
	my $average_llx = 0;
  	my $average_lly = 0;
	my $average_urx = 0;
	my $average_ury = 0;
	my $stdev_llx = 0;
	my $stdev_lly = 0;
	my $stdev_urx = 0;
	my $stdev_ury = 0;

	for (my $i=0; $i<=$#pages; $i++) {
		$average_llx += $pages[$i][0] / @pages;
	        $average_lly += $pages[$i][1] / @pages;
	        $average_urx += $pages[$i][2] / @pages;
	        $average_ury += $pages[$i][3] / @pages;
	};

	print "Averages $average_llx $average_lly $average_urx $average_ury \n" if $::opt_debug;

	for (my $i=0; $i<=$#pages; $i++) {
        
	        $stdev_llx += ( ($pages[$i][0]-$average_llx)**2 ) / @pages;
                $stdev_lly += ( ($pages[$i][1]-$average_lly)**2 ) / @pages;
                $stdev_urx += ( ($pages[$i][2]-$average_urx)**2 ) / @pages;
                $stdev_ury += ( ($pages[$i][3]-$average_ury)**2 ) / @pages;
        };
	
	print "Deviations $stdev_llx $stdev_lly $stdev_urx $stdev_ury \n" if $::opt_debug;

        $stdev_llx = sqrt( $stdev_llx);
        $stdev_lly = sqrt( $stdev_lly);
        $stdev_urx = sqrt( $stdev_urx);
        $stdev_ury = sqrt( $stdev_ury);
	
	$min_llx = $average_llx - ( $stdevp_range * $stdev_llx );
        $min_lly = $average_lly - ( $stdevp_range * $stdev_lly );
        $max_urx = $average_urx + ( $stdevp_range * $stdev_urx );
        $max_ury = $average_ury + ( $stdevp_range * $stdev_ury );

	print "Estimated rational dimensions $min_llx $min_lly $max_urx $max_ury \n" if $::opt_debug;

# Prepare auto-exclusion list

	for (my $i = 0; $i<=$#pages; $i++ ) {
		if( $pages[$i][0] < $min_llx or
		    $pages[$i][1] < $min_lly or
		    $pages[$i][2] > $max_urx or
		    $pages[$i][3] > $max_ury ) {

			push(@exclude_auto, $i+1);
			my $j=$i + 1;
			print "Excluding page $j  from calculations\n" if $::opt_verbose;

		}
	
	}
# Request user confirmation for each page
	if( $confirm_flag ) { 
		push(@exclude, @exclude_auto); 
	} else {
		print " ".@exclude_auto." pages estimated for exclusion\n";

		foreach my $i (@exclude_auto) {

			next if ( in_array($i, @exclude) );

			print "Confrim exlusion of page $i from calculations [y/N]:";
			my $answer = <STDIN>;
			chomp($answer); 
	
			if (lc($answer) eq "y" or lc($answer) eq "yes") {
				print "Page $i excluded\n";
				push (@exclude, $i);
			}

		}
	}

  }
#Calculate output dimensions

  $min_llx = 0; $min_lly = 0; $max_urx = 0; $max_ury = 0;
  for(my $i=0;$i<=$#pages;$i++) {
 	next if (in_array($i+1, @exclude));
	 if ($min_llx > $pages[$i][0] or $i == 0 ) { $min_llx = $pages[$i][0]; };
	 if ($min_lly > $pages[$i][1] or $i == 0 ) { $min_lly = $pages[$i][1]; };
	 if ($max_urx < $pages[$i][2] or $i == 0 ) { $max_urx = $pages[$i][2]; };
	 if ($max_ury < $pages[$i][3] or $i == 0 ) { $max_ury = $pages[$i][3]; };
  }

  print "Output dimensions: $min_llx $min_lly $max_urx $max_ury\n" if $::opt_verbose;
  

   for(my $i=1;$i<=$page;$i++) {

        if ($::opt_clip) {
          print TMP "\\pageclip $i [$min_llx $min_lly $max_urx $max_ury][$llx $lly $urx $ury]\n";
        }
        else {
          my ($a, $b, $c, $d) = ($min_llx - $llx, $min_lly - $ury, $max_urx + $urx, $max_ury + $lly);
          print TMP "\\page $i [$a $b $c $d]\n";
        }

   }

 }

 # auto2 mode moves box rather than resize it to fit text on the page
 if (lc ($::opt_mode) eq "auto2" ) {

# Handle page exclusion

 my @exclude_string = split ( /[\s,]+/,  $::opt_exclude);
 my $max_sizex = 0;
 my $max_sizey = 0;

 foreach my $page_word ( @exclude_string ) {
	
	if ( lc($page_word) eq "auto" ) { $auto_flag = 1; next; };
 	if ( lc($page_word) eq "fullauto" ) { $auto_flag=1; $confirm_flag = 1; next;};
	if ( int($page_word) >0 ) { push(@exclude, int($page_word) ); };
	
 }

 # If to perform auto exclusion, do some statistics - average dimensions and stdevp 
 if ( $auto_flag ) {

	print "Auto exclusion enabled \n" if $::opt_debug;
	
	my $average_sizex = 0;
  	my $average_sizey = 0;
	my $stdev_sizex = 0;
	my $stdev_sizey = 0;


	for (my $i=0; $i<=$#pages; $i++) {
		$average_sizex += abs ($pages[$i][2] - $pages[$i][0] ) / @pages;
	        $average_sizey += abs ($pages[$i][3] - $pages[$i][1] ) / @pages;
	};

	print "Averages $average_sizex $average_sizey  \n" if $::opt_debug;

	for (my $i=0; $i<=$#pages; $i++) {
        
	        $stdev_sizex += ( ($pages[$i][2] - $pages[$i][0] - $average_sizex)**2 ) / @pages;
                $stdev_sizey += ( ($pages[$i][3] - $pages[$i][1] - $average_sizey)**2 ) / @pages;
        };
	
	

        $stdev_sizex = sqrt( $stdev_sizex);
        $stdev_sizey = sqrt( $stdev_sizey);

	print "Deviations $stdev_sizex $stdev_sizey  \n" if $::opt_debug;
	
	# sensitivity is increased twice, as two dimensions influence x or y size
	$max_sizex = $average_sizex + ( $stdevp_range * $stdev_sizex / 2 ); 
        $max_sizey = $average_sizey + ( $stdevp_range * $stdev_sizey / 2 ); 

	print "Estimated rational page size $max_sizex $max_sizey  \n" if $::opt_debug;

# Prepare auto-exclusion list

	for (my $i = 0; $i<=$#pages; $i++ ) {
		if(  abs ( $pages[$i][2] - $pages[$i][0] ) > $max_sizex or
		    abs ( $pages[$i][3] - $pages[$i][1] ) > $max_sizey ) {

			push(@exclude_auto, $i+1);
			my $j=$i + 1;
			print "Excluding page $j  from calculations\n" if $::opt_verbose;

		}
	
	}
# Request user confirmation for each page
	if( $confirm_flag ) { 
		push(@exclude, @exclude_auto); 
	} else {
		print " ".@exclude_auto." pages estimated for exclusion\n";

		foreach my $i (@exclude_auto) {

			next if ( in_array($i, @exclude) );

			print "Confrim exlusion of page $i from calculations [y/N]:";
			my $answer = <STDIN>;
			chomp($answer); 
	
			if (lc($answer) eq "y" or lc($answer) eq "yes") {
				print "Page $i excluded\n";
				push (@exclude, $i);
			}

		}
	}

  }
#Calculate output dimensions

  $min_llx = 0; $min_lly = 0; $max_urx = 0; $max_ury = 0; $max_sizex = 0; $max_sizey =0;

  for(my $i=0;$i<=$#pages;$i++) {
 	next if (in_array($i+1, @exclude));
	 if ($max_sizex < abs ($pages[$i][2] - $pages[$i][0] ) or $i == 0 ) { $max_sizex = abs ($pages[$i][2] - $pages[$i][0] ); };
	 if ($max_sizey < abs ($pages[$i][3] - $pages[$i][1] ) or $i == 0 ) { $max_sizey = abs ($pages[$i][3] - $pages[$i][1] ); };
  }

  print "Output page size: $max_sizex $max_sizey\n" if $::opt_verbose;
  

   for(my $i=0;$i<=$#pages;$i++) {

	if (lc ($::opt_align)  eq "lt" ) {
			$min_llx = $pages[$i][0];
			$max_ury = $pages[$i][3];	
			$min_lly = $max_ury - $max_sizey;
			$max_urx = $min_llx + $max_sizex;
	}
		
	if (lc ($::opt_align)  eq "lb" ) {
			$min_llx = $pages[$i][0];
			$min_lly = $pages[$i][1];
			$max_ury = $min_lly + $max_sizey;
			$max_urx = $min_llx + $max_sizex;
	}

	if (lc ($::opt_align)  eq "rt" ) {
			$max_urx = $pages[$i][2];
			$max_ury = $pages[$i][3];
			$min_lly = $max_ury - $max_sizey;
			$min_llx = $max_urx - $max_sizex;
	}

	if (lc ($::opt_align)  eq "rb" ) {
			$max_urx = $pages[$i][2];
			$min_lly = $pages[$i][1];
			$max_ury = $min_lly + $max_sizey;
			$min_llx = $max_urx - $max_sizex;
	}
	
	my $j = $i + 1; 

        if ($::opt_clip) {
		
          print TMP "\\pageclip $j [$min_llx $min_lly $max_urx $max_ury][$llx $lly $urx $ury]\n";
        }
        else {
          my ($a, $b, $c, $d) = ($min_llx - $llx, $min_lly - $ury, $max_urx + $urx, $max_ury + $lly);
          print TMP "\\page $j [$a $b $c $d]\n";
        }

   }


}

close(CMD);
}

if ( lc ($::opt_mode) eq "absolute") {
  open(CMD, $cmdpipe) or
     die "$Error Cannot call pdfinfo!\n";

  my $max_ury = 0;
  my $max_urx = 0;
  $page = 0;

  while (<CMD>) {
    if (/^Pages:\s*(\d+)/) {
        $page = $1;
    }
    if ( /^Page size:\s*([\.\d]+)\sx\s([\.\d]+)/ ) {

        $max_urx=$1;
        $max_ury=$2;
        print "Page dimensions $max_urx x $max_ury\n" if $::opt_verbose;
    }
    if ( /^Page rot:\s*-?90/ ) {
        my $tmp_max = $max_urx;
        $max_urx = $max_ury;
        $max_ury = $tmp_max;
    }
  }

  close (CMD);

  for(my $i=1;$i<=$page;$i++) {
        my ($a, $b, $c, $d) = ($llx, $ury, $max_urx - $urx, $max_ury - $lly);
        print TMP "\\page $i [$a $b $c $d]\n";
  }

}
print TMP "\\csname \@\@end\\endcsname\n\\end\n";
close(TMP);

### Run pdfTeX

push @unlink_files, "$tmp.log";
if ($::opt_verbose) {
    $cmd = "$::opt_pdftexcmd -interaction=nonstopmode $tmp";
}
else {
    $cmd = "$::opt_pdftexcmd -interaction=batchmode $tmp";
}
print "* Running pdfTeX ...\n" if $::opt_verbose;
print "* pdfTeX call: $cmd\n" if $::opt_debug;
if ($::opt_verbose) {
    system($cmd);
}
else {
    `$cmd`;
}
if ($?) {
    die "$Error pdfTeX run failed!\n";
}

### Move temp file to output
rename "$tmp.pdf", $outputfile or
    die "$Error Cannot move `$tmp.pdf' to `$outputfile'!\n";

print "==> $page pages written on `$outputfile'.\n";

$exit_code = 0;
cleanup();

sub in_array() {
    my $val = shift(@_);
     
    foreach my $elem(@_) {
        if($val == $elem) {
            return 1;
        }
    }
    return 0;
}
__END__
