# Resolve o problema "Two Sum": dado um array de inteiros e um alvo,
# retorna os índices dos dois números que somam o alvo.
# Cada entrada tem exatamente uma solução, e você não pode usar o mesmo elemento duas vezes.

from typing import List

def two_sum_brute_force(nums: List[int], target: int) -> List[int]:
    """
    Força bruta: O(n^2) tempo, O(1) espaço.
    """
    # Copilot sugeriu a estrutura dos loops e a condição
    for i in range(len(nums)):
        for j in range(i + 1, len(nums)):
            if nums[i] + nums[j] == target:
                return [i, j]
    return []  # nunca acontece, pois sempre há solução

def two_sum_hash_map(nums: List[int], target: int) -> List[int]:
    """
    Dicionário: O(n) tempo, O(n) espaço.
    """
    # Copilot completou a lógica do dicionário após eu digitar "num_to_index = {}"
    num_to_index = {}
    for i, num in enumerate(nums):
        complement = target - num
        if complement in num_to_index:
            return [num_to_index[complement], i]
        num_to_index[num] = i
    return []

if __name__ == "__main__":
    # Testes gerados pelo Copilot após eu escrever "test_cases ="
    test_cases = [
        ([2, 7, 11, 15], 9),
        ([3, 2, 4], 6),
        ([3, 3], 6),
        ([1, 2, 3, 4, 5], 9),
        ([0, 4, 3, 0], 0),
    ]

    for nums, target in test_cases:
        result = two_sum_hash_map(nums, target)
        print(f"Números: {nums}, Alvo: {target} → Índices: {result}")
        # Verificação rápida sugerida pelo Copilot
        if result:
            assert nums[result[0]] + nums[result[1]] == target, "Erro na solução!"