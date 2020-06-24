{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 1,
   "metadata": {},
   "outputs": [],
   "source": [
    "import os\n",
    "import csv\n",
    "import pandas as pd"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 2,
   "metadata": {},
   "outputs": [],
   "source": [
    "full_path = os.path.join(\"Resources\",\"budget_data.csv\")"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 3,
   "metadata": {},
   "outputs": [],
   "source": [
    "reader = csv.reader(full_path)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 4,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/html": [
       "<div>\n",
       "<style scoped>\n",
       "    .dataframe tbody tr th:only-of-type {\n",
       "        vertical-align: middle;\n",
       "    }\n",
       "\n",
       "    .dataframe tbody tr th {\n",
       "        vertical-align: top;\n",
       "    }\n",
       "\n",
       "    .dataframe thead th {\n",
       "        text-align: right;\n",
       "    }\n",
       "</style>\n",
       "<table border=\"1\" class=\"dataframe\">\n",
       "  <thead>\n",
       "    <tr style=\"text-align: right;\">\n",
       "      <th></th>\n",
       "      <th>Date</th>\n",
       "      <th>Profit/Losses</th>\n",
       "    </tr>\n",
       "  </thead>\n",
       "  <tbody>\n",
       "    <tr>\n",
       "      <th>0</th>\n",
       "      <td>Jan-2010</td>\n",
       "      <td>867884</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>1</th>\n",
       "      <td>Feb-2010</td>\n",
       "      <td>984655</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>2</th>\n",
       "      <td>Mar-2010</td>\n",
       "      <td>322013</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>3</th>\n",
       "      <td>Apr-2010</td>\n",
       "      <td>-69417</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>4</th>\n",
       "      <td>May-2010</td>\n",
       "      <td>310503</td>\n",
       "    </tr>\n",
       "  </tbody>\n",
       "</table>\n",
       "</div>"
      ],
      "text/plain": [
       "       Date  Profit/Losses\n",
       "0  Jan-2010         867884\n",
       "1  Feb-2010         984655\n",
       "2  Mar-2010         322013\n",
       "3  Apr-2010         -69417\n",
       "4  May-2010         310503"
      ]
     },
     "execution_count": 4,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "data_file_df = pd.read_csv(full_path)\n",
    "data_file_df.head()\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 5,
   "metadata": {
    "tags": []
   },
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "87\n"
     ]
    }
   ],
   "source": [
    "num_rows = 0\n",
    "\n",
    "for row in open(\"Resources/budget_data.csv\"):\n",
    "    num_rows += 1\n",
    "\n",
    "print(num_rows)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 19,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "$38,382,578.00\n"
     ]
    }
   ],
   "source": [
    "total = data_file_df[\"Profit/Losses\"].sum()\n",
    "formatted_total = \"${:,.2f}\".format(total)\n",
    "print(formatted_total)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 7,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "$446,309.05\n"
     ]
    }
   ],
   "source": [
    "average = data_file_df[\"Profit/Losses\"].mean()\n",
    "formatted_average = \"${:,.2f}\".format(average)\n",
    "print(formatted_average)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 8,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "$1,170,593.00\n"
     ]
    }
   ],
   "source": [
    "max = data_file_df[\"Profit/Losses\"].max()\n",
    "formatted_max = \"${:,.2f}\".format(max)\n",
    "print(formatted_max)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 9,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Feb-2012\n"
     ]
    }
   ],
   "source": [
    "date_of_max = data_file_df[data_file_df['Profit/Losses'] == max]['Date'].values[0]\n",
    "print(date_of_max)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 10,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "$-1,196,225.00\n"
     ]
    }
   ],
   "source": [
    "min = data_file_df[\"Profit/Losses\"].min()\n",
    "formatted_min = \"${:,.2f}\".format(min)\n",
    "print(formatted_min)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 11,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Sep-2013\n"
     ]
    }
   ],
   "source": [
    "date_of_min = data_file_df[data_file_df['Profit/Losses'] == min]['Date'].values[0]\n",
    "print(date_of_min)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 14,
   "metadata": {
    "tags": []
   },
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "87\n",
      "38382578\n",
      "446309.0465116279\n",
      "1170593\n",
      "-1196225\n"
     ]
    }
   ],
   "source": [
    "print(num_rows)\n",
    "print(total)\n",
    "print(average)\n",
    "print(max)\n",
    "print(min)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 20,
   "metadata": {
    "tags": []
   },
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "This is the output of the data from our budget sheet.\n"
     ]
    }
   ],
   "source": [
    "import sys\n",
    "\n",
    "print('This is the output of the data from our budget sheet.')\n",
    "\n",
    "original_stdout = sys.stdout \n",
    "with open('Assessment/Analytics.txt', 'w') as f:\n",
    "    sys.stdout = f \n",
    "    print('Financial Analysis')\n",
    "    print('----------------------------')\n",
    "    print('Total Months:', num_rows)\n",
    "    print('Total:',formatted_total)\n",
    "    print('Average  Change:',formatted_average)\n",
    "    print('Greatest Increase in Profits:', date_of_max, formatted_max)\n",
    "    print('Greatest Decrease in Profits:', date_of_min, formatted_min)\n",
    "    sys.stdout = original_stdout "
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": []
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": []
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": []
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3.7.6 64-bit (conda)",
   "language": "python",
   "name": "python37664bitcondafa00bd6b44a14f0ab54779ea5e8fc92e"
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
   "version": "3.7.6"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 4
}
