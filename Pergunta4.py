data = {
    'SP': 67836.43,
    'RJ': 36678.66,
    'MG': 29229.88,
    'ES': 27165.48,
    'Outros': 19849.53
}

total = sum(data.values())

for state, value in data.items():
    percent = (value / total) * 100
    print(f"{state}: {value:.2f} ({percent:.2f}%)")

print(f"Total: {total:.2f}")
