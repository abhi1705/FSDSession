from schema import Schema, And, Use, SchemaError

#Cases
dat_schema = {
    'schema': Schema({
        "Sepal_Length": And(Use(float)), 
        "Sepal_Width": And(Use(float)), 
        "Petal_Length":And(Use(float)), 
        "Petal_Width": And(Use(float))
    }),
    'num_feats':4
}

check_list = {
    'length' : True,
    'schmea' : True
}

#Check
def check_length(dat_schema,data):
    return len(data.keys())==dat_schema['num_feats']

def check_schema(dat_schema, data):
    try:
        dat_schema['schema'].validate(data)
        return True
    except SchemaError:
        return False
