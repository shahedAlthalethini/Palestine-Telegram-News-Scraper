import pandas as pd
import os

folder_path = r'C:\NLP_project\task4_just_to me'
output_file = r'C:\NLP_project\task4_just_to me\merged_cleaned.csv'

standard_columns = ['Id', 'date', 'platform', 'title', 'News content', 'Label']

column_mapping = {
    'ID': 'Id',
    'id': 'Id',
    'Date': 'date',
    'date': 'date',
    'Platform': 'platform',
    'platform': 'platform',
    'Title': 'title',
    'title': 'title',
    'News content': 'News content',
    'news_content': 'News content',
    'News_Content' : 'News content',
    'content': 'News content',
    'text': 'News content',
    'News Content': 'News content',
    'Label': 'Label',
    'label': 'Label',
    'url': None,  # حذف الأعمدة غير المطلوبة
    'Unnamed: 6': None,
    'Unnamed: 7': None,
    'Unnamed: 8': None,
    'Unnamed: 9': None
}

merged_dfs = []

for filename in os.listdir(folder_path):
    if filename.endswith('.csv'):
        file_path = os.path.join(folder_path, filename)
        df = pd.read_csv(file_path)

        print("origin file",filename,df.shape)

        # توحيد أسماء الأعمدة
        df = df.rename(columns={col: column_mapping.get(col, col) for col in df.columns if column_mapping.get(col) is not None})

        # حذف الأعمدة غير المرغوبة
        df = df[[col for col in df.columns if col in standard_columns]]

        # إضافة الأعمدة المفقودة كـ NaN (لو ناقصة)
        for col in standard_columns:
            if col not in df.columns:
                df[col] = pd.NA

        # توحيد قيم Label
        label_mapping = {
            'REAL': 'real',
            'Real': 'real',
            'real': 'real',
            'FAKE': 'fake',
            'Fake': 'fake',
            'fake': 'fake',
            0 : 'real',
            1 : 'fake'
        }
        df['Label'] = df['Label'].map(label_mapping).fillna(df['Label'])


        # توحيد قيم platform
        platform_mapping = {
            'Aljazeera news': 'Aljazeera',
            'AJPalestine': 'Aljazeera',
            'Aljazeera': 'Aljazeera',
            'MisbarFC': 'Misbar',
            'Misbar': 'Misbar',
            'tibianps': 'Tibyan'
        }

        df['platform'] = df['platform'].map(platform_mapping).fillna(df['platform'])
        
        # حذف التكرار بناءً على 'title' و 'News content'
        df = df.drop_duplicates(subset=['title', 'News content'])
        print("after remove duplicates",df.shape)
        # إعادة ترتيب الأعمدة
        df = df[standard_columns]

        # حذف الصفوف التي platform فيها غير من ['Aljazeera', 'Misbar', 'Tibyan']
        #df = df[df['platform'].isin(['Aljazeera', 'Misbar', 'Tibyan'])]

        #print("after remove any other platform ",df.shape)

        # df['date'] = pd.to_datetime(df['date'], format='mixed').dt.date
        # df = df.sort_values(by='date').reset_index(drop=True)
        # df['date'] = pd.to_datetime(df['date'].astype(str), format='%Y-%m-%d')
        # print(df['date'].dtype)
        df['date'] = pd.to_datetime(df['date'], format='mixed')  # احذفي .dt.date
        df = df.sort_values(by='date').reset_index(drop=True)
        print(df['date'].dtype)
        
        
        print("Nulls per column:\n", df.isnull().sum())
        print("Unique platforms:", df['platform'].unique())
        print("Unique labels:", df['Label'].unique())
        print('record null :', df[df.isnull().any(axis=1)].shape)

        df = df.dropna(subset=['Id', 'date', 'platform', 'title', 'News content', 'Label'])


        print("final processing ",df.shape)

        merged_dfs.append(df)
        print("-----------------------------------------------------------")



# # دمج كل البيانات

final_df = pd.concat(merged_dfs, ignore_index=True)

# توليد Id من 1 إلى عدد الصفوف في الملف النهائي
final_df['Id'] = range(1, len(final_df) + 1)

# # حفظ الملف النهائي

final_df.to_csv(output_file, index=False)


print("Its files are merged and saved in:", output_file)

