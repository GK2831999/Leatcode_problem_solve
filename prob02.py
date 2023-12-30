{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 5,
   "id": "3883bfb2",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "[1, 2]\n"
     ]
    }
   ],
   "source": [
    "arr = [3,2,4]\n",
    "\n",
    "target = 6\n",
    "k = 0\n",
    "for i in arr:\n",
    "    if target-i in arr and arr.index(target-i) != k:\n",
    "        print([k,arr.index(target-i)])\n",
    "        break\n",
    "    k +=1    "
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "bfbf5a2d",
   "metadata": {},
   "outputs": [],
   "source": []
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
   "version": "3.11.5"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 5
}
