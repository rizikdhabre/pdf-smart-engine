{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "6c321afa",
   "metadata": {},
   "outputs": [],
   "source": [
    "from collections import deque\n",
    "\n",
    "def panels_for_target(target: str):\n",
    "    if target == \"A5\":\n",
    "        return 4, 2\n",
    "    if target == \"A6\":\n",
    "        return 8, 4\n",
    "    if target == \"A7\":\n",
    "        return 16, 8\n",
    "    raise ValueError(\"Unknown target\")\n",
    "\n",
    "def plan_signatures(total_pages: int, small_sig=28, large_sig=32):\n",
    "    if total_pages <= small_sig:\n",
    "        return [small_sig]\n",
    "    base_count = total_pages // small_sig\n",
    "    remainder = total_pages - base_count * small_sig\n",
    "    if remainder == 0:\n",
    "        return [small_sig] * base_count\n",
    "    conversions = 0\n",
    "    rem = remainder\n",
    "    diff = large_sig - small_sig\n",
    "    while rem > 0 and conversions < base_count:\n",
    "        conversions += 1\n",
    "        rem = remainder + conversions * diff\n",
    "        if rem % small_sig == 0:\n",
    "            break\n",
    "    sigs = [small_sig] * (base_count - conversions) + [large_sig] * conversions\n",
    "    used = sum(sigs)\n",
    "    if total_pages - used > 0:\n",
    "        sigs.append(small_sig if total_pages - used <= small_sig else large_sig)\n",
    "    while sum(sigs) < total_pages:\n",
    "        sigs.append(small_sig)\n",
    "    return sigs\n",
    "\n",
    "def paginate_signature(sig_size: int, panels_per_sheet: int):\n",
    "    pages = deque(range(1, sig_size + 1))\n",
    "    sheets = []\n",
    "    half = panels_per_sheet // 2\n",
    "    while pages:\n",
    "        group = []\n",
    "        for _ in range(half):\n",
    "            group.append(pages.pop() if pages else -1)\n",
    "            group.append(pages.popleft() if pages else -1)\n",
    "        front = group[:half]\n",
    "        back = list(reversed(group[half:]))\n",
    "        sheets.append({\"front\": front, \"back\": back})\n",
    "    return sheets\n",
    "\n",
    "def map_signature_to_global_pages(start_page: int, sig_size: int, sheets):\n",
    "    mapped = []\n",
    "    for sheet in sheets:\n",
    "        front = [(start_page + (p - 1)) if p > 0 else -1 for p in sheet['front']]\n",
    "        back = [(start_page + (p - 1)) if p > 0 else -1 for p in sheet['back']]\n",
    "        mapped.append({\"front\": front, \"back\": back})\n",
    "    return mapped\n"
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
