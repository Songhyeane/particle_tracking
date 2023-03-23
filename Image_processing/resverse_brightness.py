def reverse_brightness(frames):
    print(frames[0])
    frames = np.uint16(2 ** 16 - 1) - frames
    print(frames[0])
    return frames


rev_frames = reverse_brightness(pims.open(cropped_path + '/' + 'cropped' + original_datas_list[original_datas_index]))
# print(rev_frames[10])
plt.imshow(rev_frames[0])
