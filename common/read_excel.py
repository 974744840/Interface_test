import xlrd


class ExcelUtil():
    ''' excel表格'''
    def __init__(self,excelPath,sheetName="Sheet1"):
        '''打开表格：表对象date'''
        self.data=xlrd.open_workbook(excelPath)
        '''选择sheet：sheet对象table'''
        self.table=self.data.sheet_by_name(sheetName)
        '''要把excel里给定的sheet用table.row_types(0) 得到第一行所有内容，row_types是0开始.是列表'''
        self.keys=self.table.row_values(0)
        # print(self.keys)
        '''获取sheet里所有行数'''
        self.rowNum=self.table.nrows
        '''获取sheet里所有列数'''
        self.colNum=self.table.ncols

    def dict_data(self):
        if self.rowNum<=1:
            print('总行数小于1')
        else:
            '''这里把所有的excel表格里的数据都存在 r 列表里，
                具体的内容是以字典对应：
                r：大列表     s：字典   
                r： [
                s： {key:value,key:value,key:value}
                    {列1：行1，列1：行2，列1：行3}
                    {列2：行1，列2：行2，列2：行3}
                    {列3：行1，列3：行2，列3：行3}
                    ] 
            '''
            r=[]
            j=1
            # for i in range(3):
            for i in list(range(self.rowNum-1)):    #[0,1,2,3]
                s={}
                s['rowNum']=i+2      #这里是行的目的是不获取第一行的键值，直接从第二行开始，
                values=self.table.row_values(j)    #获取第二行的values值
                for x in list(range(self.colNum)):
                    s[self.keys[x]]=values[x]
                r.append(s)
                j+=1
            return r

# if __name__=='__main__':
#     filepath='debug_api.xlsx'
#     sheetName='Sheet1'
#     data=ExcelUtil(filepath,sheetName)
#     print(data.dict_data())

