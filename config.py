{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "e01f0bb9",
   "metadata": {},
   "outputs": [],
   "source": [
    "# config.py\n",
    "\n",
    "# Supported booklet formats and their folds\n",
    "BOOKLET_FORMATS = {\n",
    "    \"A5\": {\"folds\": 1, \"panels_per_sheet\": 4, \"panels_per_side\": 2},\n",
    "    \"A6\": {\"folds\": 2, \"panels_per_sheet\": 8, \"panels_per_side\": 4},\n",
    "    \"A7\": {\"folds\": 3, \"panels_per_sheet\": 16, \"panels_per_side\": 8}\n",
    "}\n",
    "\n",
    "# Default signature planning sizes\n",
    "SIGNATURE_SIZES = [28, 32]  # algorithm tries to balance between these\n",
    "\n",
    "# App metadata\n",
    "APP_NAME = \"PDF Smart Engine\"\n",
    "VERSION = \"1.0.0\"\n",
    "\n",
    "# Default export folder\n",
    "OUTPUT_DIR = \"output\"\n",
    "\n",
    "# PDF constraints\n",
    "ALLOWED_PAGE_SIZE = \"A4\"  # The tool expects an A4 input PDF\n"
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
