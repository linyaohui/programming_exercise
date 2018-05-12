#coding:utf-8
import xadmin
from django.template import loader
from xadmin.views import BaseAdminPlugin,ListAdminView

class ListImportExcelPlugin(BaseAdminPlugin):
    import_excel = False   #这样设置可以保证在其他模块不会出现这个导入按钮

    def init_request(self, *args, **kwargs):
        return bool(self.import_excel)

    def block_top_toolbar(self, context, nodes):
        '''重写这个函数就是在工具栏添加导入按钮'''
        nodes.append(
            loader.render_to_string('xadmin/excel/model_list.top_toolbar.format.html',
                                    context_instance=context))

xadmin.site.register_plugin(ListImportExcelPlugin, ListAdminView)