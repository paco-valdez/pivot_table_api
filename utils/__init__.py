import json


def str_max_length(length):
    return lambda x: _str_max_length(x, length)


def _str_max_length(string, length):
    if type(string) == str or type(string) == unicode:
        if not string:
            # logger.error("Value cant be empty")
            raise ValueError("Value can't be empty")

        if len(string) > length:
            # logger.error('Max length exceeded %s', length)
            raise ValueError('Max length %s exceeded' % length)
        return string
    else:
        # logger.error('String required')
        raise ValueError('String required')


def read_config(file_name):
    with open(file_name) as json_data_file:
        try:
            config = json.load(json_data_file)
        except ValueError as ex:
            raise ValueError('Config file malformed')
    return config
