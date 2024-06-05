
def series_sum(k):
    return 6 / (2 * k - 1) * ((-1) ** (k - 1) / (2 * 3 * k - 1))

# ������������ ���� �� �������� 10^-6
series_sum_value = 0
k = 1
while True:
    term = series_sum(k)
    series_sum_value += term
    if abs(term) < 1e-6:
        break
    k += 1

print(f"�������� ����� ���� = {series_sum_value:.10f}, ���������� ������ = {k}")
