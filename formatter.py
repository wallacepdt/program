import xlrd
import csv
import os
import shutil


def construct_excel1(source):
    loc = (source)
    wb = xlrd.open_workbook(loc)

    values = []
    for i in range(wb.nsheets):
        sheet = wb.sheet_by_index(i)
        sid = i+1
        for j in range(1, sheet.nrows):
            row = sheet.row_values(j)
            if row[0] == '':
                print('\n\n\n')
            else:
                scid = int(float(row[0]))
                sn = int(float(row[1]))
                formatSn = '{}'.format('0' + str(sn)) if sn < 10 else str(sn)
                cn1 = row[2].encode('utf-8').decode('utf-8-sig')
                cn2 = row[3].encode('utf-8').decode('utf-8-sig')
                pt = row[4].encode('utf-8').decode('utf-8-sig')
                mediaPath = '/conversation/'
                soundPath = 'chat_' + str(sid) + '_' + str(scid) + '_' + formatSn + '.mp3'
                finalPath = mediaPath + soundPath

                #print((int(sid), scid, sn, cn1, cn2, pt, soundPath))
                values.append((int(sid), scid, sn, cn1, cn2, pt, finalPath))

                soundName = row[5].replace('/sounds/', '')
                
                src_dir= './media_files/'
                dst_dir= './output/media_files/'
                if not os.path.exists(dst_dir):
                    os.makedirs(dst_dir)
                src_file = os.path.join(src_dir, soundName)
                shutil.copy(src_file, dst_dir)

                old_file = os.path.join(dst_dir, soundName)
                new_file = os.path.join(dst_dir, soundPath)
                os.rename(old_file, new_file)

                print(old_file + '   ->   ' + new_file + '\n')

    with open('./output/output.txt', 'w', encoding='utf-8') as text_file:
        for line in values:
            print('{},'.format(line), file=text_file)

    print('success')
    return values
    


#construct_excel1('Chat_2019.xlsx')


def construct_excel2(source):
    loc = (source)
    wb = xlrd.open_workbook(loc)

    values = []
    for i in range(wb.nsheets):
        sheet = wb.sheet_by_index(i)
        sid = i+1
        for j in range(1, sheet.nrows):
            row = sheet.row_values(j)
            if row[0] == '' and row[2] == '':
                print('\n\n\n')
            else:
                scid = int(float(row[0])) if row[0] != '' else scid
                sn = int(float(row[2]))

                cn1 = row[3].encode('utf-8').decode('utf-8-sig')
                cn2 = row[4].encode('utf-8').decode('utf-8-sig')
                pt = row[5].encode('utf-8').decode('utf-8-sig')

                lowerPt = row[5].lower()
                soundPath =  '/vocabulary/sounds/' + lowerPt + '.mp3'
                picturePath = '/vocabulary/pics/' + lowerPt + '.jpg'

                print((scid, sn, cn1, cn2, pt, soundPath, picturePath))
                values.append((scid, sn, cn1, cn2, pt, soundPath, picturePath))

                soundName = row[6].replace('/sounds/', '')
                newSoundName = lowerPt + '.mp3'
                
                src_dir= './media_files/'
                dst_dir= './output/media_files/'
                if not os.path.exists(dst_dir):
                    os.makedirs(dst_dir)
                if row[6] != '':
                    src_file = os.path.join(src_dir, soundName)
                    shutil.copy(src_file, dst_dir)

                    old_file = os.path.join(dst_dir, soundName)
                    new_file = os.path.join(dst_dir, newSoundName)
                    os.rename(old_file, new_file)

                    print(old_file + '   ->   ' + new_file + '\n')

    with open('./output/output.txt', 'w', encoding='utf-8') as text_file:
        for line in values:
            print('{},'.format(line), file=text_file)

    print('success')
    return values



#construct_excel2('Vocab_2019.xlsx')

def construct_csv(source):
    values = []
    with open(source, newline='') as csv_file:
        bn = os.path.basename(source)
        tid = bn.replace('.csv', '')
        data = list(csv.reader(csv_file, delimiter='\n'))
        count = 0
        for row in range(1, len(data)):
            count = count + 1
            rowSplit = data[row][0].split('\t')
            temp = tid, count, rowSplit[2].encode('utf-8').decode('utf-8-sig'), rowSplit[3].encode('utf-8').decode('utf-8-sig')
            print(temp)
            values.append(temp)

    with open(source.replace('.csv', '.txt'), 'w', encoding='utf-8') as text_file:
        for line in values:
            ft = '\t'.join(map(str, line))
            print('{}'.format(ft), file=text_file)

    print('success')
    return values            



construct_csv('./csv/WCPTC665.csv')
