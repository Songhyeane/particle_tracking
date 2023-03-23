def line_select_callback(eclick, erelease):
    'eclick and erelease are the press and release events'
    x1, y1 = eclick.xdata, eclick.ydata
    x2, y2 = erelease.xdata, erelease.ydata
    print("(%3.2f, %3.2f) --> (%3.2f, %3.2f)" % (x1, y1, x2, y2))
    print(" The button you used were: %s %s" % (eclick.button, erelease.button))

    global x_range
    global y_range

    x_range = [x1, x2]
    y_range = [y1, y2]


rs = RectangleSelector(ax, line_select_callback,
                       useblit=False, button=[1, 3],
                       minspanx=5, minspany=5, spancoords='pixels',
                       interactive=True)
plt.show()

crop_img_array = img_array[:][0][int(y_range[0]):int(y_range[1]), int(x_range[0]):int(x_range[1])]

fig, ax = plt.subplots(frameon=False)
ax.axis('off')
imgs = ax.imshow(crop_img_array, cmap='gray')

plt.show()

for i in range(len(img_array[:])):
    crop_img_array = img_array[:][i][int(y_range[0]):int(y_range[1]), int(x_range[0]):int(x_range[1])]
    # print(crop_img_array.shape)
    if i == 0:
        nd_array_stack = np.array([crop_img_array])
    else:
        nd_array_stack = np.concatenate((nd_array_stack, [crop_img_array]), axis=0)

print(nd_array_stack.shape)
print(nd_array_stack)

# %%
converted_data = nd_array_stack
print(nd_array_stack)
print(type(nd_array_stack))
tiff.imwrite(cropped_path + '/' + 'cropped' + original_datas_list[original_datas_index], converted_data,
             photometric='minisblack')
