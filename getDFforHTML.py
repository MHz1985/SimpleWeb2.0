import pandas as pd
import numpy as np
import re
import copy
import html2text


def get_cols_inside_data(df):
  if len(df) > 0:
    my_dict_all={}
    indx=0
    for col in df:
      text = str(df.iloc[indx][col])
      if ":" and "{" and "}" in text :
        vals = re.findall(r"'(.*?)'", text[text.index('{')+1 : text.index('}')])
        matched_remove = copy.deepcopy(text)
        for i in vals:
          matched_remove = matched_remove.replace(i,'')
        matched_removed2=matched_remove[matched_remove.index('{')+1 : matched_remove.index('}')]
        keys=[i[:i.index(':')] for i in matched_removed2.split(", ") if ':' in i]
        my_dict={}
        my_dict = dict(zip(keys, vals))
        my_dict_all.update(my_dict)
    my_cols = list(dict.keys(my_dict_all))
    return my_cols
  else:
    return

def get_new_row_df(df,indx):
  if len(df) > 0:
    my_dict_all={}
    for col in df:
      text = str(df.iloc[indx][col])
      if ":" and "{" and "}" in text :
        vals = re.findall(r"'(.*?)'", text[text.index('{')+1 : text.index('}')])
        matched_remove = copy.deepcopy(text)
        for i in vals:
          matched_remove = matched_remove.replace(i,'')
        matched_removed2=matched_remove[matched_remove.index('{')+1 : matched_remove.index('}')]
        keys=[i[:i.index(':')] for i in matched_removed2.split(", ") if ':' in i]
        my_dict={}
        my_dict = dict(zip(keys, vals))
        if (len(keys) != len(vals)) and 'authorName' in keys:
          my_dict['authorName'] = vals[-1]
        my_dict_all.update(my_dict)
    return my_dict_all
  else:
    return

def get_full_df_html(df):
    if len(df) > 0 and (":" and "{" in str(df)):
        my_cols = get_cols_inside_data(df)
        df_new = pd.DataFrame(columns=my_cols)
        indx = 0
        new_row = get_new_row_df(df,indx)
        df_new = pd.concat([pd.DataFrame([new_row]),df_new.loc[:]]).reset_index(drop=True)
        # df_new.index = np.arange(1,len(df)+1)
        if len(df)>1 :
            for i in range(1, len(df)):
                new_row = get_new_row_df(df,i)
                df_new = pd.concat([pd.DataFrame([new_row]),df_new.loc[:]]).reset_index(drop=True)
            df_new.index = np.arange(1,len(df_new)+1)
        return df_new
    else:
        df.index = np.arange(1,len(df)+1)
        return df
    
def get_short_df_html(df, cols_short=['Id', 'authorName', 'doi', 'fullJournalName', 'title']):
    df_new=get_full_df_html(df)
    cols_full = list(df_new.columns)
    common_l = list(np.intersect1d(cols_full, cols_short))
    if len(common_l)>0:
        return df_new[common_l]
    else: 
        return df_new
    

def get_table_html_data(text):
  html_text = html2text.html2text(text)
  text_line = html_text.split(' \n')
  text_data = [i.replace('\n','').split("|") for i in text_line]
  for line in text_data:
    for data in line:
      data = str(f"u\'{data}\'")
  if len(text_data)>1:
      del text_data[1] # removing divider between header and data
  return text_data
    