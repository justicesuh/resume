import yaml
from pathlib import Path

from fpdf import FPDF
from fpdf.enums import Align, CellBordersLayout, XPos, YPos


class Resume:
    ENDASH = '\u2013'

    def __init__(self, config: Path):
        self.config = config
        self.load_data()

        self.rows = []

        self.pdf = FPDF()

        self.pdf.add_font('Helvetica Neue', style='', fname='HelveticaNeue.otf')
        self.pdf.add_font('Helvetica Neue', style='b', fname='HelveticaNeueBold.otf')
        self.pdf.set_font('Helvetica Neue')

        self.pdf.add_page()
        self.pdf.set_margins(12.5, 12.5, 12.5)

        self.page_width = self.pdf.w - self.pdf.l_margin - self.pdf.r_margin
        self.line_height = 8

    def load_data(self):
        with open(self.config, 'r') as f:
            self.data = yaml.safe_load(f)

    def add_heading(self, text: str, font_size: float):
        self.pdf.set_font_size(font_size)
        self.pdf.cell(self.page_width, self.line_height, text=text, align=Align.C, new_x=XPos.LMARGIN, new_y=YPos.NEXT)

    def add_row(self, data: list[str]):
        row = []
        colspan = 2 if len(data) == 1 else 1
        for text in data:
            row.append((text, colspan))
        self.rows.append(row)

    def _generate_table(self):
        with self.pdf.table(col_widths=(1, 1), first_row_as_headings=False, markdown=True) as table:
            for cell in self.rows:
                for text, colspan in cell:
                    row = table.row()
                    row.cell(text, colspan=colspan, border=CellBordersLayout.NONE)

    def output(self):
        self._generate_table()
        self.pdf.output(self.config.with_suffix('.pdf'))


def main():
    resume = Resume(Path('resume.yaml'))

    resume.add_heading(resume.data['name'], 24)
    resume.add_heading(resume.data['heading'], 12)

    experiences = resume.data['sections']['experiences']
    resume.add_row(['**PROFESSIONAL EXPERIENCES**'])
    for experience in experiences:
        resume.add_row([
            f"**{experience['company']}** {Resume.ENDASH} {experience['title']}"
        ])

    resume.output()


if __name__ == '__main__':
    main()
