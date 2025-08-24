from PyInstaller.utils.hooks import collect_data_files
datas = collect_data_files('tiktoken')
print("Collected data files:")
for d in datas:
    print(d)
