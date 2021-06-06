import os
from transliterate import translit, get_available_language_codes
from googletrans import Translator
import pandas as pd
import cyrtranslit
from transformers import AutoModel, BertTokenizerFast,BertModel,AutoTokenizer
tokenizer = AutoTokenizer.from_pretrained('DeepPavlov/rubert-base-cased')
translator=Translator()
    
listOfSubCorpora = os.listdir('./Data')
# print(listOfSubCorpora)


dirName = './Data/'
# sub_corpora_2=dirName+listOfSubCorpora[2]
# listOfFiles = os.listdir(sub_corpora_2)
# listOfSubCorpora=['CLassical_Prose']
# listOfSubCorpora=['Modern_Prose']
listOfSubCorpora=['Russian_Wiki']
sentence_paths=list()
for i in listOfSubCorpora:
    listOfFiles = os.listdir(dirName+i)
    file_name_dict=dict()
    incomplete_context=[]
    for mwe_path in listOfFiles:
        # print (mwe_path)
        text = str(mwe_path)
        # ru_text=translit(text, 'ru')
        ru_text=cyrtranslit.to_cyrillic(text, 'ru')
        ru_text=ru_text.replace('_',' ')
        file_name_dict[mwe_path]=ru_text
        for (dirpath, dirnames, filenames) in os.walk(dirName+i+'/'+mwe_path):
            # print(dirpath, dirnames, filenames)
            if (len(filenames) < 1) & (len(dirnames)<1):
                # print(dirpath,mwe_path)
                incomplete_context.append(mwe_path)
            elif len(dirnames)<1:
                # print(dirpath, dirnames, filenames)
                for fn in filenames:
                    sentence_paths.append(str(dirpath+'/'+fn))
# print(sentence_paths)
j=0
k=0
par3=0
par1=0
print(len((sentence_paths)))
m=[]
sentences=[]
for i in sentence_paths:
    mwe=i.split('/')[3][:-2]
    label=i.split('/')[3][-1]
    # ru_mwe=translit(mwe, 'ru')
    ru_mwe=cyrtranslit.to_cyrillic(mwe, 'ru')
    ru_mwe=ru_mwe.replace('_',' ')
    # print(ru_mwe)

    with open(i,'r',encoding='utf-8') as f:
        contents=f.read()
        par_1=contents[:contents.find('\n')]
        contents=contents[contents.find('\n')+1:]
        par_2=contents[:contents.find('\n')]
        par_3=contents[contents.find('\n')+1:]
        # print(par_2.find(ru_mwe))
        if ru_mwe== "балансироват на грани":
            ru_mwe="балансировать на грани"
        elif ru_mwe=="выше себыа":
            ru_mwe="выше себя"
        elif ru_mwe=="смотрет в лизо":
            ru_mwe="смотреть в лицо"
        elif ru_mwe=="смотрет в глаза":
            ru_mwe="смотреть в глаза"
        elif ru_mwe=="поставит точку":
            ru_mwe="поставить точку"
        elif ru_mwe=="выворачиват наизнанку":
            ru_mwe="выворачивать наизнанку"
        elif ru_mwe=="против течениыа":
            ru_mwe="против течения"
        elif ru_mwe=="выворачивает наизнанку":
            ru_mwe="выворачивает наизнанку"
        elif ru_mwe=="подныат руку":
            ru_mwe="поднять руку"
        elif ru_mwe=="плыт по течениыу":
            ru_mwe="плит по течению"
        elif ru_mwe=="ходит на задних лапах":
            ru_mwe="ходить на задних лапах"
        elif ru_mwe=="с пенои у рта":
            ru_mwe="с пеной у рта"
        elif ru_mwe=="за поыас заткнут":
            ru_mwe="за пояс заткнуть"
        elif ru_mwe=="на своыу голову":
            ru_mwe="на свою голову"
        elif ru_mwe=="плыт по течению":
            ru_mwe="плит по течению"
        elif ru_mwe=="последняя каплыа":
            ru_mwe="последняя капля"
        elif ru_mwe=="гладит по голове":
            ru_mwe="гладить по голове"
        elif ru_mwe=="мутит воду":
            ru_mwe="мутит воду"
        elif ru_mwe=="последныаыакаплыа":
            ru_mwe="последняякапля"
        elif ru_mwe=="удар ниже поыаса":
            ru_mwe="удар ниже пояса"
        elif ru_mwe=="косои взгляд":
            ru_mwe="косой взгляд"
        elif ru_mwe=="последnjая капля":
            ru_mwe="последняя капля"
        elif ru_mwe=="посмотрет в лизо":
            ru_mwe="посмотреть в лицо"
        max_seq_len=0
        
        ru_mwe_list=ru_mwe.split()
        if par_2.find(ru_mwe) == -1:
            
            # j+=1
            # print("counter:",j)
            if par_3.find(ru_mwe) > 0:
                # print("In par_3")
                # par3+=1
                # print("par3:",par3)
                par_3_words=par_3.split()
                # print(par_3_words.index(ru_mwe_list[0]),par_3_words.index(ru_mwe_list[1]))
                # print(par_3.find(ru_mwe_list[1]),par_3.find(ru_mwe))
                # print(ru_mwe,par_3[par_3.find(ru_mwe):par_3.find(ru_mwe)+10])
                if(par_3.find(ru_mwe)-300)<0:
                    sentences.append([ru_mwe,label,par_3[:600],'3'])
                    tr=tokenizer.tokenize(par_3[:600])
                    max_seq_len=max(max_seq_len,len(tr))
                    m.append(len(tr))
                elif par_3.find(ru_mwe)+300> len(par_3):
                    sentences.append([ru_mwe,label,par_3[-600:],'3'])
                    tr=tokenizer.tokenize(par_3[-600:])
                    max_seq_len=max(max_seq_len,len(tr))
                    m.append(len(tr))

                else:
                    sentences.append([ru_mwe,label,par_3[par_3.find(ru_mwe)-300:par_3.find(ru_mwe)+300],'3'])
                    tr=tokenizer.tokenize(par_3[par_3.find(ru_mwe)-300:par_3.find(ru_mwe)+300])
                    max_seq_len=max(max_seq_len,len(tr))
                    m.append(len(tr))

            elif par_1.find(ru_mwe) > 0:
                # print("In par_1 -------------------------------------")
                # par1+=1
                # print("par1:",par1)
                if(par_1.find(ru_mwe)-300)<0:
                    sentences.append([ru_mwe,label,par_1[:600],'1'])
                    tr=tokenizer.tokenize(par_3[:600])
                    max_seq_len=max(max_seq_len,len(tr))
                    m.append(len(tr))

                elif par_1.find(ru_mwe)+300> len(par_1):
                    sentences.append([ru_mwe,label,par_1[-600:],'1'])
                    tr=tokenizer.tokenize(par_1[-600:])
                    max_seq_len=max(max_seq_len,len(tr))
                    m.append(len(tr))

                else:
                    sentences.append([ru_mwe,label,par_1[par_1.find(ru_mwe)-300:par_1.find(ru_mwe)+300],'1'])
                    tr=tokenizer.tokenize(par_1[par_1.find(ru_mwe)-300:par_1.find(ru_mwe)+300])
                    max_seq_len=max(max_seq_len,len(tr))
                    m.append(len(tr))

                # sentences.append([ru_mwe,label,par_1[par_1.find(ru_mwe)-300:par_1.find(ru_mwe)+300],'1'])
            else:
                print(i, ru_mwe)
            # else:
            #     print("Second Translator...")
            #     ru_mwe=translator.translate(mwe, dest='ru').text
            #     ru_mwe=ru_mwe.replace('_',' ')
            #     print(ru_mwe)
            #     # print("using second translator.")
            #     if par_2.find(ru_mwe) > 0:
            #         sentences.append([ru_mwe,label,par_2,'2'])
            #         # print("we are in luck!")
            #     else:
            #         if par_1.find(ru_mwe) > 0:
            #             # print("In par_3")
            #             # par3+=1
            #             # print("par3:",par3)
            #             sentences.append([ru_mwe,label,par_3,'3'])
            #         elif par_1.find(ru_mwe) > 0:
            #             # print("In par_1 -------------------------------------")
            #             # par1+=1
            #             # print("par1:",par1)
            #             sentences.append([ru_mwe,label,par_1,'1'])
        else:
            k+=1
            # print("real sentences:",k)
            if(par_2.find(ru_mwe)-300)<0:
                sentences.append([ru_mwe,label,par_2[:600],'2'])
                tr=tokenizer.tokenize(par_2[:600])
                max_seq_len=max(max_seq_len,len(tr))
                m.append(len(tr))

            elif par_2.find(ru_mwe)+300> len(par_2):
                sentences.append([ru_mwe,label,par_2[-600:],'2'])
                tr=tokenizer.tokenize(par_2[-600:])
                max_seq_len=max(max_seq_len,len(tr))
                m.append(len(tr))

            else:
                sentences.append([ru_mwe,label,par_2[par_2.find(ru_mwe)-300:par_2.find(ru_mwe)+300],'2'])
                tr=tokenizer.tokenize(par_2[par_2.find(ru_mwe)-300:par_2.find(ru_mwe)+300])
                # max_seq_len=max(max_seq_len,len(tr))
                m.append(len(tr))

            # sentences.append([ru_mwe,label,par_2[par_2.find(ru_mwe)-64:par_2.find(ru_mwe)+64],'2'])
print(len(sentences))
print(max(m))
df = pd.DataFrame.from_records(sentences)
df.columns=["mwe","label","sentence","par"]
# df.to_excel('sentences_classic.xlsx',index=False)
# df.to_excel('sentences_modern.xlsx',index=False)
df.to_excel('sentences_wiki_1404_w_300.xlsx',index=False)
