def check_nesting_depth(node) -> int:
    """
    Функция для проверки уровня вложенности
    :param node: Node
    :return level: int
    """
    if node.supplier is None:
        return 0
    else:
        return 1 + check_nesting_depth(node.supplier)
