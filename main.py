from webscraping.examples.ex2.By_bs4 import By_bs4
import xlsxwriter

class Wt_table(object):

    xls_book=xlsxwriter.Workbook('/Users/addseq/Desktop/liepin.xlsx')
    sheet=xls_book.add_worksheet('sheet')

    def __init__(self,lists):
        self.lists=lists
        self.wr()

    def wr(self):
        row=0
        for value in lists:
            for i in range(0,6):
                self.sheet.write(row,i,value[i])
            row+=1
        self.close_workbook()


    def close_workbook(self):
        self.xls_book.close()

if __name__=='__main__':

    test=By_bs4(0,1)
    lists=test.wait_write_lists
    Wt_table(lists)