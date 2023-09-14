
def image_compare_gray(image_compare_base, img2gray):
    return image_compare_base != img2gray


def image_compare_rgb(a, b):
    return a[0] != b[0] and a[1] != b[1] and a[2] != b[2]


def image_comparison(image_path_list, out_path, image_size=None, zoom_value=1.0, diff_color=(255, 165, 0), is_mode_gray=True):
    """逐像素比较图片

    从 image_path_list 中获取图片，然后依次将图片逐像素比较，将不同颜色的像素
    以指定颜色标出，以指定的图片尺寸或缩放率输出比较结果图片.

    参数:
        image_path_list: 要比较的图片的路径的列表.
        out_path: 输出的图片的路径.
        image_size: 以长宽元组的形式确定目标图片的尺寸，例如(1920, 1080)，不指定则以
                    缩放率确定目标图片的尺寸.
        zoom_value: 以缩放率的形式指定目标图片的尺寸，例如0.5.
        diff_color: 以RGB元组的形式指定不同像素的标出颜色.
        is_mode_gray: 灰度模式.

    返回:
        无.

    抛出:
        无.
    """

    import cv2
    import numpy as np
    image_base = None

    for image_path in image_path_list:
        # load image and resize
        image = cv2.imread(image_path)
        if image_size is None:
            image_size = (
                int(np.size(image, 1) * zoom_value),
                int(np.size(image, 0) * zoom_value)
            )
        image = cv2.resize(image, image_size)
        # gray
        if is_mode_gray:
            img2gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
        # pixel-by-pixel comparison
        if image_base is None:
            image_base = image
            image_compare_base = img2gray
        else:
            h, w = image.shape[0], image.shape[1]
            for i in range(w):
                for j in range(h):
                    if is_mode_gray:
                        if image_compare_gray(image_compare_base[j][i],
                                                img2gray[j][i]):
                            image_base[j][i] = (diff_color[::-1])
                    else:
                        if image_compare_rgb(image_base[j][i], image[j][i]):
                            image_base[j][i] = (diff_color[::-1])

    cv2.imwrite(out_path, image_base)


def test_image_comparison():
    img_path_A = 'imageA.png'
    img_path_B = 'imageB.png'
    comparison_result_path = 'imageC.png'
    image_comparison([img_path_A, img_path_B], comparison_result_path)


if __name__ == '__main__':
    test_image_comparison()
