from fpdf import FPDF
import pandas as pd

pdf = FPDF(orientation="P", unit='mm', format='A4')
pdf.set_auto_page_break(auto=False, margin=0)

df = pd.read_csv(r'./resources/topics.csv')

line_inc = 10
begin_title_page = 21
end_title_page = 281
begin_normal_page = 21
end_normal_page = 281
counter = 0
for index, row in df.iterrows():
    # title page
    pdf.add_page()
    counter += 1
    # header
    pdf.set_font(family='Times', size=24)
    pdf.set_text_color(100, 100, 100)
    pdf.cell(w=0, h=12, txt=row['Topic'], align='L', ln=1)
    # lines
    for height in range(begin_title_page,end_title_page+line_inc,line_inc):
        print(height)
        pdf.line(10, height, 200, height)
    # set footer
    pdf.ln(260)
    pdf.set_font(family='Times', size=8)
    pdf.set_text_color(180, 180, 180)
    pdf.cell(w=0, h=10, txt=f"{row['Topic']}-{counter}", align='R')

    for i in range(row['Pages']-1):
        # subpages
        pdf.add_page()
        counter += 1
        for height in range(begin_title_page, end_title_page + line_inc, line_inc):
            print(height)
            pdf.line(10, height, 200, height)
        # set footer
        pdf.ln(272)
        pdf.set_font(family='Times', size=8)
        pdf.set_text_color(180, 180, 180)
        pdf.cell(w=0, h=10, txt=f"{row['Topic']}-{counter}", align='R')


pdf.output(r'output_with_lines.pdf')
