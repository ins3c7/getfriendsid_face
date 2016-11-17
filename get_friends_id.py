f = open('ids_para_adicionar.txt', 'a')

ids=[];x=1;espaco=0

print 'baixando...'
soup = bs(bro.page_source, "html.parser");
print 'compelto! a gravar..'

for i in soup.findAll('div', attrs= {'class':'fsl fwb fcb'}):
  if espaco > 80:
    f.write('\n\n\n\n\n\n\n\n\n\n')
    espaco=0
  try:
    idz=i.a['data-gt'].split('"eng_tid":"')[1].split('"')[0]
    if idz not in ids:
      print 'gravando:', str(x);x+=1
      gravar = '<div class="tokenarea" style="" id="u_7_6"><span class="removable uiToken"><span class="uiTokenText">Douglas Ruivo</span><input type="hidden" value="'+idz+'" name="members[]" autocomplete="off"><input type="hidden" value="Douglas Ruivo" name="text_members[]" autocomplete="off"><a href="#" aria-label="Remove Douglas Ruivo" class="remove uiCloseButton uiCloseButtonSmall"></a></span></div>\n'
      f.write(gravar)
      ids.append(idz)
  except:
    pass

f.close()