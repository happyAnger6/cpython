#"rmon <Integer> ":unique_group->(1,2,3):indexes->(1,2):maximum->(10):autoid->(0-1,0,1024,5):check->(insert,)
def cmd_def(*arg, **kwargs):
        pass

class UniqueGroup:
        pass

cmd_def(cmd="rmon <Integer>",
        unique_groups=[
                UniqueGroup(ID=1,Elements=[1,2,3])
        ],
        indexs=[1],
        max_num=20
        )