import sqlparse
 
query = """
-- layer0
-- table difinite start
select
  id AS user_is --name user_id  type int
  , name AS user_name --name user_name type string
-- table difinite end
from users
where id > 10;--cln
/*
test space
*/
"""
parsed_queries = sqlparse.parse(query)
tokens = list(parsed_queries[0].flatten())

column_infos = {}
name_flag=False
column_name=None
for t in tokens:
    print("token_value: '{}', token_type: {}".format(t.value, t.ttype))
    if (str(t.ttype) == 'Token.Name'):
        name_flag = True
        column_name=t.value
    else:
        if (str(t.ttype) =='Token.Text.Whitespace'):
            pass
        elif (str(t.ttype) =='Token.Comment.Single') and name_flag==True:
            column_infos[column_name]=t.value
            name_flag=False
            print('***')
            print(t)
            print('***')
        else:
            name_flag=False
            column_name=None
print(column_infos)
#print([column_info.value for column_info in column_infos])
