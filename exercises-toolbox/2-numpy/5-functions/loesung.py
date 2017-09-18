#! /usr/bin/env python
# encoding: utf-8

import numpy as np


A = np.arange(5)


print(f"Array A: {A}")

# Lösung zu 1)
print("\tnp.sum(A):", np.sum(A))
print("\tnp.diff(A):", np.diff(A))
print("\tnp.prod(A):", np.prod(A))
print("\tnp.mean(A):", np.mean(A))
print("\tnp.std(A):", np.std(A))


B = np.array([[2, 1, 2, 1, 2], [1, 2, 1, 2, 1], [3, 1, 3, 1, 3]])


print(f"Array B:\n{B}")

# Lösung zu 2)
print("\tnp.sum(B):", np.sum(B))
print("\tnp.sum(B, axis=0):", np.sum(B, axis=0))
print("\tnp.sum(B, axis=1):", np.sum(B, axis=1))
print("\tnp.sum(B, axis=(0,1)):", np.sum(B, axis=(0, 1)))
print("\tnp.diff(B):\n", np.diff(B))
print("\tnp.diff(B, axis=0):\n", np.diff(B, axis=0))
print("\tnp.diff(B, axis=1):\n", np.diff(B, axis=1))
print("\tnp.prod(B):", np.prod(B))
print("\tnp.prod(B, axis=0):", np.prod(B, axis=0))
print("\tnp.prod(B, axis=1):", np.prod(B, axis=1))
print("\tnp.prod(B, axis=(0,1)):", np.prod(B, axis=(0, 1)))
print("\tnp.mean(B):", np.mean(B))
print("\tnp.mean(B, axis=0):", np.mean(B, axis=0))
print("\tnp.mean(B, axis=1):", np.mean(B, axis=1))
print("\tnp.mean(B, axis=(0,1)):", np.mean(B, axis=(0, 1)))
print("\tnp.std(B):", np.std(B))
print("\tnp.std(B, axis=0):", np.std(B, axis=0))
print("\tnp.std(B, axis=1):", np.std(B, axis=1))
print("\tnp.std(B, axis=(0,1)):", np.std(B, axis=(0, 1)))


# Lösung 3)
data = np.loadtxt("einkauf.txt")
print("Daten\n", data)

sum_per_person = np.sum(data, axis=0)
print("Summe pro Person:", sum_per_person)

sum_data = np.sum(data)
print("Gesamtsumme:", sum_data)

mean_per_person = np.mean(data, axis=0)
print("Mittel pro Person:", mean_per_person)

sum_per_day = np.sum(data, axis=1)
print("Summe pro Tag:", sum_per_day)

mean_per_day = np.mean(data, axis=1)
print("Mittel pro Tag:", mean_per_day)