import PyPDF2

# 打开原始pdf文件
with open('C:\\Users\\17901\\Desktop\\研一上作业\\故障诊断原理与应用\\SX2303167-韩阿东-故障诊断原理与应用报告.pdf', 'rb') as f:
    pdf_reader = PyPDF2.PdfFileReader(f)

    # 创建一个新的pdf写入器
    pdf_writer = PyPDF2.PdfFileWriter()

    # 遍历每一页pdf文件
    for page_num in range(pdf_reader.getNumPages()):
        # 跳过18和19页，从0开始计数
        if page_num == 1 :
            continue

        # 获取当前页面并添加到新的pdf文件中
        page = pdf_reader.getPage(page_num)
        pdf_writer.addPage(page)

    # 将新的pdf文件写入磁盘
    with open('C:\\Users\\17901\\Desktop\\研一上作业\\故障诊断原理与应用\\SX2303167-韩阿东-故障诊断原理与应用报告2.pdf', 'wb') as out_file:
        pdf_writer.write(out_file)
