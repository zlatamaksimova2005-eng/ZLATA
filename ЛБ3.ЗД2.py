def find_common_participants(group1: str, group2: str, separator: str = ",") -> list[str]:

    participants1 = group1.split(separator)
    participants2 = group2.split(separator)

    common = set(participants1) & set(participants2)

    return sorted(common)



participants_first_group = "Иванов|Петров|Сидоров"
participants_second_group = "Петров|Сидоров|Смирнов"

common_participants = find_common_participants(
    participants_first_group, participants_second_group, "|"
)
print("Общие участники:", common_participants)
