import yaml

from fpdf import FPDF
from fpdf.enums import Align, XPos, YPos


def main():
    with open('resume.yaml', 'r') as f:
        data = yaml.safe_load(f)

    pdf = FPDF()
    pdf.add_page()
    pdf.set_font('Helvetica', size=24)

    pdf.cell(pdf.w - pdf.l_margin - pdf.r_margin, 8, text=data['name'], align=Align.C, new_x=XPos.LMARGIN, new_y=YPos.NEXT)
    pdf.set_font_size(12)
    pdf.cell(pdf.w - pdf.l_margin - pdf.r_margin, 8, text=data['heading'], align=Align.C, new_x=XPos.LMARGIN, new_y=YPos.NEXT)

    pdf.output('resume.pdf')


if __name__ == '__main__':
    main()
