{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "8e3ca39e",
   "metadata": {},
   "outputs": [],
   "source": [
    "import fitz  # PyMuPDF\n",
    "\n",
    "def render_sheet_to_pdf(src_doc: fitz.Document, page_numbers_front, page_numbers_back, a4_width=595, a4_height=842):\n",
    "    new = fitz.open()\n",
    "\n",
    "    panels_per_side = len(page_numbers_front)\n",
    "    cols = 1 if panels_per_side == 1 else 2\n",
    "    rows = panels_per_side // cols\n",
    "\n",
    "    # FRONT\n",
    "    front_page = new.new_page(width=a4_width, height=a4_height)\n",
    "    idx = 0\n",
    "    for c in range(cols):\n",
    "        for r in range(rows):\n",
    "            if idx >= panels_per_side:\n",
    "                break\n",
    "            panel_w = a4_width / cols\n",
    "            panel_h = a4_height / rows\n",
    "            x0 = c * panel_w\n",
    "            y0 = r * panel_h\n",
    "            rect = fitz.Rect(x0, y0, x0 + panel_w, y0 + panel_h)\n",
    "            pnum = page_numbers_front[idx]\n",
    "            if pnum != -1:\n",
    "                src = src_doc.load_page(pnum - 1)\n",
    "                mat = fitz.Matrix(min(panel_w / src.rect.width, panel_h / src.rect.height),\n",
    "                                  min(panel_w / src.rect.width, panel_h / src.rect.height))\n",
    "                pix = src.get_pixmap(matrix=mat, alpha=False)\n",
    "                img_rect = fitz.Rect(rect.x0, rect.y0, rect.x0 + pix.width, rect.y0 + pix.height)\n",
    "                front_page.insert_image(img_rect, pixmap=pix)\n",
    "            idx += 1\n",
    "\n",
    "    # BACK\n",
    "    back_page = new.new_page(width=a4_width, height=a4_height)\n",
    "    idx = 0\n",
    "    for c in range(cols):\n",
    "        for r in range(rows):\n",
    "            if idx >= panels_per_side:\n",
    "                break\n",
    "            panel_w = a4_width / cols\n",
    "            panel_h = a4_height / rows\n",
    "            x0 = c * panel_w\n",
    "            y0 = r * panel_h\n",
    "            rect = fitz.Rect(x0, y0, x0 + panel_w, y0 + panel_h)\n",
    "            pnum = page_numbers_back[idx]\n",
    "            if pnum != -1:\n",
    "                src = src_doc.load_page(pnum - 1)\n",
    "                mat = fitz.Matrix(min(panel_w / src.rect.width, panel_h / src.rect.height),\n",
    "                                  min(panel_w / src.rect.width, panel_h / src.rect.height))\n",
    "                pix = src.get_pixmap(matrix=mat, alpha=False)\n",
    "                img_rect = fitz.Rect(rect.x0, rect.y0, rect.x0 + pix.width, rect.y0 + pix.height)\n",
    "                back_page.insert_image(img_rect, pixmap=pix)\n",
    "            idx += 1\n",
    "\n",
    "    return new\n"
   ]
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3 (ipykernel)",
   "language": "python",
   "name": "python3"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.10.9"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 5
}
