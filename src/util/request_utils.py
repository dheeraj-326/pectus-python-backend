from src.data.expanses_repository import get_fields


def params_to_query(params: dict):
    field_names = get_fields()
    all_expressions = {}
    for key, value in params.items():
        if '[' in key:
            name, operator = key.split('[', 2)
            operator = operator[:-1]
            if name not in field_names:
                continue
            expression = None
            if operator == 'gte':
                expression = '>='
            elif operator == 'lte':
                expression = '<='
            elif operator == 'ge':
                expression = '>'
            elif operator == 'le':
                expression = '<'
        else:
            expression = '=='
            if name not in field_names:
                continue
        all_expressions = update_expressions(expression, name, value, all_expressions)
    return make_query_string(all_expressions)


def make_query_string(all_expressions):
    operations = []
    for field, expressions in all_expressions.items():
        for expression, value in expressions.items():
            if not str(value).isnumeric():
                operation = f"`{field}` {expression} '{value}'"
            else:
                operation = f"`{field}` {expression} {value}"
            operations.append(operation)
    query_string = ' & '.join(operations)
    return query_string


def update_expressions(expression, name, value, all_expressions):
    if expression:
        if name not in all_expressions:
            expressions = {
                expression: value
            }
        else:
            expressions = all_expressions[name]
            if expression in expressions:
                raise Exception(f'{expression} can be specified only once for {name}')
            expressions[expression] = value
        all_expressions[name] = expressions
    return all_expressions
