#coding:utf-8
from django.shortcuts import render
import xadmin
from .models import Product
from xadmin import  views
import xlrd

class GlobalSettings(object):
    site_title="programming exercise"
    site_footer="programming exercise"
    menu_style="accordion"

class ProductAdmin(object):
    list_display=['name','cost_price','list_price','description']
#    search_fields = ['name', 'cost_price', 'list_price', 'description']
    list_filter=['name', 'cost_price', 'list_price', 'description']
    import_excel = True

    def post(self,request,*args,**kwargs):
        '''处理前端提交来的excel文件'''
        if 'excel' in request.FILES:
            excel = xlrd.open_workbook(
                filename=None, file_contents=request.FILES.get('excel').read())  # 关键点在于这里
            product_list = []
            table = excel.sheets()[0]
            nrows = table.nrows
            ncols = table.ncols
            HEAD = ['name', 'cost_price', 'list_price', 'description']
            table_head = table.row_values(0)
            if table_head != HEAD:
                render(request, "500.html", {'msg': '数据头部错误，必须是' + "['name', 'standard_price', 'list_price', 'description']" + "，顺序不可变！"})

            else:
                for i in range(nrows):
                    if i > 0:
                        product_list.append(table.row_values(i))
                try:
                    self.insertProduct(product_list)
                except:
                    pass
        return super(ProductAdmin, self).post(request,args,kwargs)

    def insertProduct(self,product_list):
        for item in product_list:
            try:
                sc = Product()
                sc.name = item[0]
                sc.cost_price = item[1]
                sc.list_price = item[2]
                sc.description = item[3]
                sc.save()
            except:
                raise Exception("error")

xadmin.site.register(Product,ProductAdmin)
xadmin.site.register(views.CommAdminView,GlobalSettings)