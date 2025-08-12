{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "bcb6ab2d",
   "metadata": {},
   "outputs": [],
   "source": [
    "import sys\n",
    "from PyQt6.QtWidgets import QApplication\n",
    "from gui import BookletMakerGUI\n",
    "\n",
    "def main():\n",
    "    app = QApplication(sys.argv)\n",
    "    win = BookletMakerGUI()\n",
    "    win.show()\n",
    "    sys.exit(app.exec())\n",
    "\n",
    "if __name__ == \"__main__\":\n",
    "    main()\n"
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
