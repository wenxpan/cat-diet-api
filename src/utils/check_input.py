from marshmallow.validate import ValidationError

def check_input_category(data, valid_categories):
    # validate function that checks if the 'category' field in request body 
    # belongs to one of the set categories

    # only validate when category is in the request body
    if data.get('category'):
        # check if input is in one of the defined categories, case insensitive
        category = [x for x in valid_categories if x.upper() ==
                    data['category'].upper()]
        if len(category) == 0:
            # raise error if no match
            raise ValidationError(
                f'Category must be one of: {valid_categories}')
        # return value with correct case
        data['category'] = category[0]