# from django.utils import timezone
# from djbook.settings import USE_TZ, TIME_ZONE
#
#
# today = timezone.now()
#
# day1 = today.weekday()
# day = 0 if   > 6 else today.isoweekday()
#
# ff = day



def get_table_data(from_file, table_name):
    with open(from_file, 'r') as f:
        line = f.readline()
        while line:
            if line.find('COPY ' + table_name + ' (')>-1:
                with open('/home/alp/' + table_name + '_r.sql', 'w') as f2:
                    f2.write('SET search_path = \'denoc2010\';\n')
                    f2.write('SET client_encoding = \'WIN1251\';\n')
                    f2.write(line)
                    for i in xrange(1, 509):
                            line = f.readline()
                            # print i + ':' + line.decode(encoding='CP1252').encode(encoding='CP1251')
                            f2.write(line)
                    break
            line = f.readline()




get_table_data('/home/alp/198_150514.sql', 'kadastr_m_r')



# with open('/home/alp/198_150514.sql', 'r') as f:
#     line = f.readline()
#     while line:
#         if line.find('COPY denooc_rayon (gid')>-1:
#             with open('/home/alp/denooc_rayon.sql', 'w') as f2:
#                 f2.write('SET search_path = \'denoc2010\';\n')
#                 f2.write('SET client_encoding = \'WIN1251\';\n')
#                 f2.write(line)
#                 for i in xrange(1, 509):
#                         line = f.readline()
#                         # print i + ':' + line.decode(encoding='CP1252').encode(encoding='CP1251')
#                         f2.write(line)
#                 break
#         line = f.readline()
