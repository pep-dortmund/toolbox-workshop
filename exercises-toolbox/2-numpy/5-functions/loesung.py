#! /usr/bin/env python
# encoding: utf-8

import numpy as np

A = np.arange(5)

# begin solution
# Ganz wichtig: KEINE PANIK!
# Diese Lösung ist etwas lang, das sollte dich aber nicht abschrecken, die
# meisten Zeilen sind print-Funktionen. Es geht hier nicht darum, die
# Lösung 1 zu 1 nachzuarbeiten,sondern darum, ein Gefühl dafür zu bekommen,
# wie die numpy Funktionen in unterschiedlichen Dimensionen funktionieren.

print("Aufgabe 1)")
print(f"Array A: {A}")
# end solution

# Lösung zu 1) hier:
# begin solution
print("\tnp.sum(A):", np.sum(A))
print("\tnp.diff(A):", np.diff(A))
print("\tnp.prod(A):", np.prod(A))
print("\tnp.mean(A):", np.mean(A))
print("\tnp.std(A):", np.std(A))
print("\tnp.min(A):", np.min(A))
print("\tnp.max(A):", np.max(A))
# end solution


B = np.array([[2, 1, 2, 1, 2], [1, 2, 1, 2, 1], [3, 1, 3, 1, 3]])

# Lösung zu 2) hier:

# begin solution
print("Aufgabe 2)")
print(f"Array B:\n{B}")

print("\tnp.sum(B):", np.sum(B))
print("\tnp.sum(B, axis=0):", np.sum(B, axis=0))
print("\tnp.sum(B, axis=1):", np.sum(B, axis=1))
print("\tnp.sum(B, axis=(0,1)):", np.sum(B, axis=(0, 1)))
print()
print("\tnp.diff(B):\n", np.diff(B))
print("\tnp.diff(B, axis=0):\n", np.diff(B, axis=0))
print("\tnp.diff(B, axis=1):\n", np.diff(B, axis=1))
print()
print("\tnp.prod(B):", np.prod(B))
print("\tnp.prod(B, axis=0):", np.prod(B, axis=0))
print("\tnp.prod(B, axis=1):", np.prod(B, axis=1))
print("\tnp.prod(B, axis=(0,1)):", np.prod(B, axis=(0, 1)))
print()
print("\tnp.mean(B):", np.mean(B))
print("\tnp.mean(B, axis=0):", np.mean(B, axis=0))
print("\tnp.mean(B, axis=1):", np.mean(B, axis=1))
print("\tnp.mean(B, axis=(0,1)):", np.mean(B, axis=(0, 1)))
print()
print("\tnp.std(B):", np.std(B))
print("\tnp.std(B, axis=0):", np.std(B, axis=0))
print("\tnp.std(B, axis=1):", np.std(B, axis=1))
print("\tnp.std(B, axis=(0,1)):", np.std(B, axis=(0, 1)))
print()
print("\tnp.min(B):", np.min(B))
print("\tnp.min(B, axis=0):", np.min(B, axis=0))
print("\tnp.min(B, axis=1):", np.min(B, axis=1))
print("\tnp.min(B, axis=(0,1)):", np.min(B, axis=(0, 1)))
print()
print("\tnp.max(B):", np.max(B))
print("\tnp.max(B, axis=0):", np.max(B, axis=0))
print("\tnp.max(B, axis=1):", np.max(B, axis=1))
print("\tnp.max(B, axis=(0,1)):", np.max(B, axis=(0, 1)))
# end solution

# Lösung zu 3) hier:
# begin solution
data = np.genfromtxt("einkauf.txt")

print("Aufgabe 3)")
print("Daten\n", data)

sum_per_person = np.sum(data, axis=0)
print("\nSumme pro Person:", sum_per_person)

mean_per_person = np.mean(data, axis=0)
print("\nÜber die Tage gemittelte Ausgaben pro Person:\n", mean_per_person)

sum_data = np.sum(data)
print("\nGesamtsumme:", sum_data)

sum_per_day = np.sum(data, axis=1)
print("\nSumme pro Tag:\n", sum_per_day)

mean_per_day = np.mean(data, axis=1)
print("\nÜber die Personen gemittelte Ausgaben pro Tag:\n", mean_per_day)

min_per_person = np.min(data, axis=0)
print("\nMinimalausgabe pro Person", min_per_person)

max_per_person = np.max(data, axis=0)
print("\nMaximalausgabe pro Person", max_per_person)

min_per_day = np.min(data, axis=1)
print("\nMinimalausgabe pro Tag", min_per_day)

max_per_day = np.max(data, axis=1)
print("\nMaximalausgabe pro Tag", max_per_day)


print("\nAufgabe 3d) keepdims=True")

sum_per_person = np.sum(data, axis=0, keepdims=True)
print("\nSumme pro Person:", sum_per_person)

mean_per_person = np.mean(data, axis=0, keepdims=True)
print("\nÜber die Tage gemittelte Ausgaben pro Person:\n", mean_per_person)

sum_data = np.sum(data, keepdims=True)
print("\nGesamtsumme:", sum_data)

sum_per_day = np.sum(data, axis=1, keepdims=True)
print("\nSumme pro Tag:\n", sum_per_day)

mean_per_day = np.mean(data, axis=1, keepdims=True)
print("\nÜber die Personen gemittelte Ausgaben pro Tag:\n", mean_per_day)

min_per_person = np.min(data, axis=0, keepdims=True)
print("\nMinimalausgabe pro Person", min_per_person)

max_per_person = np.max(data, axis=0, keepdims=True)
print("\nMaximalausgabe pro Person", max_per_person)

min_per_day = np.min(data, axis=1, keepdims=True)
print("\nMinimalausgabe pro Tag", min_per_day)

max_per_day = np.max(data, axis=1, keepdims=True)
print("\nMaximalausgabe pro Tag", max_per_day)
# end solution
