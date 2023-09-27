import fitz

def pdf2image(pdfPath, imgPath, extension=".png", zoom_x=10, zoom_y=10, rotation_angle=0):
    # 打开PDF文件
    pdf = fitz.open(pdfPath)
    # 逐页读取PDF
    for pg in range(0, pdf.page_count):
        page = pdf[pg]
        # 设置缩放和旋转系数
        trans = fitz.Matrix(zoom_x, zoom_y).prerotate(rotation_angle)
        pm = page.get_pixmap(matrix=trans, alpha=False)
        # 开始写图像
        pm.save(imgPath + str(pg) + extension)
    pdf.close()

def test_pdf2image():
    pdfPath = 'imageA.png'
    pdfPath = 'imageB.png'
    pdf2image(pdfPath, pdfPath)

def test_pdf2image_and_gettime():
    import time
    start_time = time.perf_counter()
    test_pdf2image()
    print('execution time: ' + (time.perf_counter() - start_time) + ' s')
