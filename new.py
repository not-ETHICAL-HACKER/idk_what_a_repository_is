import time
import sys
def effect(txt:str)->None:
    for i in txt:
        sys.stdout.write(i)
        sys.stdout.flush()
        time.sleep(1e-3)
effect("""sƃuᴉlǝǝɟ ɹnoʎ ʇɹnɥ oʇ ʇou noʎ uo ʎsɐǝ oƃ ɐuuoƃ sɐʍ I 'ʞoo⅂                                                                           
(sǝʇnuᴉw xᴉs 'sǝʇnuᴉw xᴉs) ǝɔuɐɥɔ ǝuo sᴉɥʇ ʇǝƃ oʇ ,uᴉoƃ ʎluo w,I ʇnB                                                                 
(uo ǝɹ,noʎ 'ʎpɐɥS wᴉlS 'sǝʇnuᴉw xᴉs) ʇᴉ lǝǝɟ uɐɔ I 'ƃuoɹʍ s,ƃuᴉɥʇǝwoS                                                                
(sǝʇnuᴉw xᴉs 'xᴉs 'sǝʇnuᴉw xᴉs) ʇɐɥʍ ʍouʞ ʇ,uop I ʇnq 'uǝddɐɥ oʇ ʇnoqɐ s,ƃuᴉɥʇǝwos ǝʞᴉl 'ʇoƃ ǝʌ,I ,uᴉlǝǝɟ ɐ ʇsnſ                     
ǝlqnoɹʇ ƃᴉq 'ǝlqnoɹʇ uᴉ ǝɹ,ǝʍ 'suɐǝw ʇᴉ ʞuᴉɥʇ I ʇɐɥʍ suɐǝw ʇɐɥʇ ɟI                                                                   
(pǝɹǝpɹo ɔop ǝɥʇ ʇɐɥʍ ʇsnɾ ǝɹɐ noʎ) sǝɔuɐɥɔ ʎuɐ ,uᴉʞɐʇ ʇou w,I 'ʎɐs noʎ sɐ sɐuɐuɐq sɐ sᴉ ǝɥ ɟᴉ pu∀                                   
po⅁ dɐᴚ 'po⅁ dɐᴚ ɐ ǝʞᴉl lǝǝɟ oʇ ,uᴉuuᴉƃǝq w,I                                                                                        
pou ʞɔɐq 'pou ʞɔɐq ǝɥʇ oʇ ʇuoɹɟ ǝɥʇ woɹɟ ǝldoǝd ʎw ll∀                                                                               
¿xoq dɐls 'xoq dɐls oʇ ɥƃnouǝ ƃuol ǝɹɐ swɹɐ ɹᴉǝɥʇ sʞuᴉɥʇ oɥʍ 'ʍoᴎ                                                                    
ʇoq-dɐᴚ ǝw llɐɔ os 'ʇoqoɹ ɐ ǝʞᴉl dɐɹ I pᴉɐs ʎǝɥ⊥                                                                                     
ʇǝʞɔod ʞɔɐq ʎw uᴉ doʇdɐl ɐ ʇoƃ I 'sǝuǝƃ ʎw uᴉ ǝq ʇsnw ʇᴉ ɹǝʇndwoɔ ɐ ǝʞᴉl dɐɹ oʇ ǝw ɹoɟ ʇnB                                           
ʇᴉɟoɹd dɐɹ ʇɐɥʇ woɹɟ ʇouʞ ʇɐɟ ɐ ʇoƃ 'ʇᴉ ʞɔoɔ-ɟlɐɥ I uǝɥʍ ɟɟo oƃ ll,uǝd ʎW                                                            
ǝɔᴉɟɟo uᴉ llᴉʇs sɐʍ uoʇuᴉlↃ llᴉB ǝɔuᴉs ɹǝʌǝ 'ʇᴉ ɟɟo ,uᴉllᴉʞ ɐ puɐ ,uᴉʌᴉl ɐ ǝpɐW                                                      
ʞɔɐs - sᴉɥ uo ,uᴉlǝǝɟ ʎʞsuᴉʍǝ⅂ ɐɔᴉuoW ɥʇᴉM                                                                                           
llǝɥ llɐ sɐ ʇuǝɔǝpuᴉ sɐ puɐ ǝpnɹ sɐ ʇnq 'ʇsǝuoɥ sɐ llᴉʇs ↃW uɐ w,I                                                                   
(ɥʇᴉʍ llɐ wǝ, llᴉʞ) ɔᴉloɥ-ɐ-llᴉʞs 'sǝlqɐllʎS                                                                                         
ɥɔʇɐw ,uᴉssᴉd ɐ oʇuᴉ ʇǝƃ ɐuuɐʍ ʎllɐǝɹ ʇ,uop noʎ 'doɥ-dᴉɥ ʎʇᴉddᴉɥ-ʎʇᴉddᴉp ʎʇᴉddᴉlɟ sᴉɥ⊥                                               
ʞɔɐʎ-ʎʇǝʞɔɐʎ 'dɐʎ-dɐʎ 'dɐɹɔ dɐɹ ʞɔɐdʞɔɐq ',ɔ∀ ǝɥʇ ɟo ʞɔɐq ǝɥʇ uᴉ Ↄ∀W ɐ ,uᴉʞɔɐd 'ʇɐɹq ʎʇᴉddɐɹ sᴉɥʇ ɥʇᴉM                               
ʇɐɥʇ ,uᴉɔᴉʇɔɐɹd w,I ǝlᴉɥʍ sʇunʇs ʇɐqoɹɔɐ lɐɔᴉɹʎl ǝsǝɥʇ ʇdwǝʇʇɐ I 'ǝwᴉʇ ǝwɐs ʇɔɐxǝ ǝɥʇ ʇɐ pu∀                                         
ɟlɐɥ uᴉ ʇᴉ ʞɔɐɹɔ puɐ - ɟo ǝldnoɔ ɐ ɟo ʞɔɐq ǝɥʇ ɹǝʌo ǝlqɐʇ -ɹǝɥʇow ɐ ʞɐǝɹq oʇ ǝlqɐ ǝq llᴉʇs ll,I                                      
ʇɔɐɟ ǝɥʇ ɹǝʇɟɐ ɥʇɐwɹǝʇɟ∀ oʇ pǝuƃᴉs sɐʍ I 'ɔᴉuoɹᴉ sɐʍ ʇᴉ pǝzᴉlɐǝɹ ʎluO                                                                
ʞɔɐʇʇɐ ɟo ɥʇɐɹʍ ʎw lǝǝɟ 'sqwoq-Ⅎ doɹp sᴉ op I ll∀ ¿ʍolq ʇou I plnoɔ ʍoH                                                              
pɐd ᴉxɐw ɐ s,ǝɹǝɥ 'poᴉɹǝd ǝwᴉʇ ɥƃnoɹ ɐ ,uᴉʌɐɥ ǝɹɐ sɹǝddɐᴚ                                                                            
ǝɔᴉdɹǝʇsɐw sᴉɥʇ ,uᴉʇɔnɹʇsuoɔ ʎllnɟɹǝʇsɐw w,I ǝlᴉɥʍ ʞɔɐʍ ǝɥʇ ɹoɟ pɐq ʎlsnoɹʇsɐsᴉp ʎllɐnʇɔɐ s,ʇI                                       
po⅁ dɐᴚ 'po⅁ dɐᴚ ɐ ǝʞᴉl lǝǝɟ oʇ ,uᴉuuᴉƃǝq w,I ǝsnɐↃ,                                                                                 
pou ʞɔɐq 'pou ʞɔɐq ǝɥʇ oʇ ʇuoɹɟ ǝɥʇ woɹɟ ǝldoǝd ʎw ll∀                                                                               
¿xoq dɐls 'xoq dɐls oʇ ɥƃnouǝ ƃuol ǝɹɐ swɹɐ ɹᴉǝɥʇ sʞuᴉɥʇ oɥʍ 'ʍoᴎ                                                                    
pɹɐɥ ʇɐɥʇ 'pɹɐɥ ʇɐɥʇ ʇ,uᴉɐ -ɥs sᴉɥʇ ,uᴉuᴉɐʇuᴉɐw noʎ ʍoɥs ǝw ʇǝ⅂                                                                      
ʇoƃ ǝʌɐɥ  ǝʞᴉl ʎʇᴉlɐʇɹowᴉ dɐɹ oʇ ʇǝɹɔǝs ǝɥʇ puɐ ʎǝʞ ǝɥʇ ʇuɐʍ ʎpoqʎɹǝʌƎ                                                              
ǝɔuɐɹǝqnxǝ lnɟɥʇnoʎ puɐ ǝƃɐɹ ʎldwᴉs 's,ʇuᴉɹdǝnlq ǝɥʇ lnɟɥʇnɹʇ ǝq oʇ 'llǝM                                                            
pᴉoɹǝʇsɐ uɐ ǝʞᴉl ɥʇɹɐƎ ǝɥʇ ʇᴉɥ 'ǝɔuɐsᴉnu ɐ ɹoɟ ʇooɹ oʇ sǝʌol ʎpoqʎɹǝʌƎ                                                               
(ʍǝd) ǝɔuᴉs uooW ǝɥʇ ɹoɟ ʇooɥs ʇnq ,uᴉɥʇou pᴉᗡ                                                                                       
„ǝwʎɥɹ ǝɥʇ snB„ 'oʇ ǝlɔᴉɥǝʌ ɐ sɐ ʇᴉ ǝsn I ǝsnɐɔ, ɔᴉsnw sᴉɥʇ ɥʇᴉʍ looɥɔs oʇ uǝʞɐʇ ʇǝƃ sↃW                                             
sʇuǝpnʇs ɟo llnɟ looɥɔs ʍǝu ɐ pɐǝl I ʍoᴎ                                                                                             
uǝᴚ 'ɔoᗡ ʎǝɥ 'ǝqnↃ '∀˙M˙ᴎ 'ɔɐԀᄅ 'zzɐqɐɥS wᴉʞɐ⅂ 'wᴉʞɐᴚ ɟo ʇɔnpoɹd ɐ w,I ¿ǝW                                                           
wᴉlS ʇoƃ ʎǝɥʇ 'noʎ ʞuɐɥʇ 'ʎzɐƎ 'ɐllǝ⅄                                                                                                
uoᴉʇᴉsod ɐ uᴉ ǝq puɐ dn ʍolq 'dn ʍoɹƃ ʎɐp ǝuo oʇ ɥƃnouǝ pǝɹᴉdsuI                                                                     
-ɹǝɥʇow ǝɥʇ oʇuᴉ wǝɥʇ ʇɔnpuᴉ puɐ '˙Ↄ˙W˙ᗡunᴚ ʇǝǝw o⊥                                                                                  
sǝwɐlɟ ɟo llɐq ɐ uᴉ ʇsɹnq puɐ ɥɔɹnɥɔ ǝɥʇ uᴉ ʞlɐʍ ll,I ɥƃnoɥʇ uǝʌǝ ǝwɐℲ ɟo llɐH lloᴚ puɐ ʞɔoᴚ                                         
(ǝwɐɥs) ɟo llɐʍ ǝɥʇ uo ǝwɐɟ ɟo loɥoɔlɐ ǝɥʇ sᴉ uᴉ pǝʇɔnpuᴉ ǝq ll,I ǝwɐℲ ɟo llɐH ʎluO                                                  
sǝwɐlɟ ɟo ʞɔolɟ ɐ ʞlɐʍ I lᴉʇ, ǝwɐƃ ɐ llɐ s,ʇᴉ ʞuᴉɥʇ - no⅄                                                                            
¿,uᴉʞuᴉɥʇ noʎ ǝɹɐ - ǝɥʇ uᴉ ʇɐɥʍ ǝw llǝʇ 'puɐ ʞuɐld ɐ ɟɟO                                                                             
(ɐɥɐɥ) ʎoq ,uᴉʞool 'ǝɔɐɟ ʇɥƃᴉɐɹʇs ɐ ɥʇᴉʍ ʇᴉ ʎɐs ʎlǝɹɐq uɐɔ I -ƃ os 'ʎoq ,uᴉʞool-ƃ ǝlʇʇᴉ⅂                                             
ʎoq ,uᴉʞool 'ǝɔɐld ǝʞɐʇ ,uᴉɹǝɥʇɐƃ ɥɔɹnɥɔ ɐ ,uᴉɥɔʇɐʍ ǝɹ,noʎ ǝʞᴉl ɹnɔɔo-ssɐw ɐ ,uᴉssǝuʇᴉʍ ǝɹ,no⅄                                       
ʎoq ,uᴉʞool 'ʎɐs ʎǝɥʇ llɐ s,ʇɐɥʇ '„-ƃ s,ʎoq ʇɐɥʇ 'ʎǝʌ ʎO„                                                                            
ʎoq ,uᴉʞool 'ʎɐp ʎɹǝʌǝ lǝqɐl ɹnoʎ woɹɟ „oƃ oʇ ʎɐM„ 'ɐ puɐ ʞɔɐq ǝɥʇ uo ʇɐd 'dn sqwnɥʇ ɐ ʇǝƃ no⅄                                       
ʎoq ,uᴉʞool 'ǝɹᗡ woɹɟ „ɥɐǝʎ llǝH„ 'ɐ ʇǝƃ I ¿ʎoq ,uᴉʞool 'ʎɐs noʎ ʇɐɥʍ 'ʎoq ,uᴉʞool 'ʎǝH                                              
ʎoq ,uᴉʞool 'ǝɔɐɟ ʎw ɐʇʇno ʇǝƃ '-s ɹoɟ ʎpoqou pǝʞsɐ ɹǝʌǝu 'ǝʌɐɥ I ,uᴉɥʇʎɹǝʌǝ ɹoɟ ʞɹoʍ ɐw,I                                           
ǝsnɐɔ, 'ʎoq ,uᴉʞool 'ǝɔɐd ǝwɐs ǝɥʇ ɥʇᴉʍ dn ,uᴉdǝǝʞ ɟo ǝlqɐdɐɔ ǝq ɐuuoƃ ɹǝʌǝu ǝɹ,noʎ 'ʎoq 'ʎllɐɔᴉsɐB                                  
po⅁ dɐᴚ 'po⅁ dɐᴚ ɐ ǝʞᴉl lǝǝɟ oʇ ,uᴉuuᴉƃǝq w,I                                                                                        
pou ʞɔɐq 'pou ʞɔɐq ǝɥʇ oʇ ʇuoɹɟ ǝɥʇ woɹɟ ǝldoǝd ʎw ll∀                                                                               
ᴚ∀ↃS∀ᴎ 'ᴚ∀ↃS∀ᴎ ǝw llɐɔ 'ʞɔɐɹʇ ǝɥʇ punoɹɐ ,uᴉɔɐɹ w,I ʎɐʍ ǝɥ⊥                                                                          
po⅁ ɥsɐɹ⊥ ǝʇᴉɥM ǝɥʇ 'ʞɹɐd ɹǝlᴉɐɹʇ ǝɥʇ ɟo ʇpɹɐɥuɹɐƎ ǝlɐᗡ                                                                              
pɹɐƃs∀ 'pɹɐƃs∀ 'ou 'uoʇdʎɹ⋊ s,ʇǝuɐld sᴉɥʇ 'poZ lɐɹǝuǝ⅁ ǝɹoɟǝq lǝǝu⋊                                                                  
ʇuǝʇodᴉuwo w,I 'ʇuǝpoɹ noʎ 'uᴉpO ǝq ll,I puɐ 'ɹoɥ⊥ ǝq ll,noʎ oS                                                                      
,uᴉʇoʇ w,I sqwoq ǝsǝɥʇ ɥʇᴉʍ ʎlǝʇɐᴉpǝwᴉ ',uᴉpɐolǝɹ w,I uǝɥʇ 'ɟɟo ʇǝ⅂                                                                 
uǝʞoʍ ǝq ʇou plnoɥs I pu∀                                                                                                            
-dǝǝp wow ɹnoʎ ʇoƃ I ʇnq ',uᴉʇɐolɟ ǝᴉqwoz ɐ 'pɐǝɥ ,uᴉʞlɐʇ ɐ ʇsnɾ w,I ʇnq 'pɐǝp ,uᴉʞlɐʍ ǝɥʇ w,I                                       
ǝlpood 'uowoɔ uᴉ ,uᴉɥʇou ǝʌɐɥ ǝʍ 'ǝlpooᴎ uǝwɐᴚ ʎw ʇno w,I                                                                           
lᴉdnd 'ǝƃɐwoɥ ʎɐd puɐ wɹɐ ǝɥʇ uᴉ ɟlǝsɹnoʎ ɥɔuᴉd 'uɐwɹǝqoᗡ ɐ w,I                                                                      
lɐʇnɹq s,ʎʇsǝuoɥ ʎw 'ǝw s,ʇI                                                                                                         
ɥƃnoɥʇ op I ʇɐɥʍ ǝzᴉlᴉʇn ʇ,uop I ɟᴉ ǝlᴉʇnɟ ʎlʇsǝuoɥ s,ʇᴉ ʇnB                                                                         
ǝlᴉɥʍ ɐ uᴉ ǝɔuo ʇsɐǝl ʇɐ 'pooƃ ɹoℲ                                                                                                   
sǝwʎɥɹ ɥƃnouǝ ǝlpoop puɐ ǝlqqᴉɹɔs I ɥɔʇɐɹɔs uǝʞɔᴉɥɔ sᴉɥʇ uᴉ ǝɹǝɥʍǝwos ǝɹns ǝʞɐw ɐuuɐʍ I oS                                           
sǝwᴉʇ ɥƃnoʇ ɥƃnoɹɥʇ ǝldoǝd ǝwos ʇǝƃ dlǝɥ oʇ ʎɹʇ ǝqʎɐw o⊥                                                                             
pǝuƃᴉsun noʎ uǝʌǝ ǝsnɐɔ, ǝsɐɔ uᴉ ʇsnɾ sǝuᴉlɥɔund ʍǝɟ ɐ dǝǝʞ ɐʇʇoƃ I ʇnB                                                              
ǝwᴉʇɥɔunl s,ʇᴉ ǝʞᴉl ǝw ʇɐ ,uᴉʞool ʎɹƃunɥ ǝɹɐ sɹǝddɐᴚ                                                                                 
punoɹƃɹǝpun ǝɥʇ ɟo ƃuᴉʞ sɐʍ I ǝɔuo ǝɹǝɥʍ ǝwᴉʇ ɐ sɐʍ ǝɹǝɥʇ ʍouʞ I                                                                     
puᴉɹƃ ɥɔuoW ǝɥɐoɹɐɥԀ ʎw uo w,I ǝʞᴉl dɐɹ llᴉʇs I ʇnB                                                                                  
ǝuᴉqwoɔ noʎ uǝɥʍ sǝwᴉʇǝwos ʇnq 'sǝwʎɥɹ ɥɔunɹɔ I oS                                                                                   
ǝuᴉw ɟo ɹoloɔ uᴉʞs ǝɥʇ ɥʇᴉʍ lɐǝdd∀                                                                                                   
ǝuᴉl ǝuo ʇɐɥʇ ǝʞᴉl noʎ ɹosuǝɔ oʇ ,uᴉʎɹʇ ǝwoɔ ʎǝɥʇ ǝɹǝɥ puɐ ƃᴉq ooʇ ʇǝƃ no⅄                                                           
ǝuᴉqwnloↃ woɹɟ -ʞ uǝʌǝs ǝʞɐʇ ll,I ʎɐs oʇ pǝᴉɹʇ I uǝɥʍ Ɩ Ԁ⅂ sɹǝɥʇɐW ǝɥ⊥ woɹɟ „ʞɔɐB w,I„ 'uo pᴉɐs I                                    
6˙ ɐ puɐ ɹǝʌloʌǝɹ ɐ 'Ɫᔭ-⋊∀ uɐ ppɐ 'ǝuᴉl ɐ uᴉ llɐ wǝ, ʇnԀ                                                                             
w,I ʇnq 'sɐʍ I sɐ ƃᴉq sɐ ʇ,uᴉɐ I ʇɐɥʇ ʍou ʇᴉ ɥʇᴉʍ ʎɐʍɐ ʇǝƃ I ɟᴉ ǝǝS                                                                  
lɐʇɹod ǝɥʇ ɥƃnoɹɥʇ ,uᴉwoɔ 'lɐʇɹowᴉ uɐ oʇuᴉ ,uᴉɥdɹoW                                                                                 
ɥƃnoɥʇ ᔭ00ᄅ woɹɟ dɹɐʍ ǝwᴉʇ ɐ uᴉ ʞɔnʇs ǝɹ,no⅄                                                                                         
ɹoɟ ǝwʎɥɹ noʎ ʇɐɥʇ -ɟ ǝɥʇ ʇɐɥʍ ʍouʞ ʇ,uop I pu∀                                                                                      
sʍoɹuɹoɔ ,uᴉʞɔ- ɥʇᴉʍ lǝzundɐᴚ sɐ ssǝlʇuᴉod ǝɹ,no⅄                                                                                    
lɐwɹou ,uᴉǝq -Ⅎ ¿lɐwɹou ǝʇᴉɹʍ no⅄                                                                                                    
ǝɹnʇnɟ ǝɥʇ woɹɟ unƃʎɐɹ ʍǝu ɐ ʇɥƃnoq ʇsnɾ I pu∀                                                                                       
pɐw ſ ʎɐᴚ ǝpɐw snoloqɐℲ uǝɥʍ ǝʞᴉl 'ɐʎ ʇooɥs puɐ ǝwoɔ oʇ ʇsnſ                                                                         
ouɐᴉd pǝʎɐld ǝɥ ǝlᴉɥʍ uɐw ɐ oʇ ,uᴉƃuᴉs pɐd s,ɹǝɥʇɐǝʍʎɐW ʇɐ - ɐ ǝʞᴉl pǝʞool ǝɥ pᴉɐs qɐℲ ǝsnɐↃ,                                        
lǝuuɐɥɔ ǝlqɐɔ ǝɥʇ uo lɐᴉɔǝds Ɫ-ᔭᄅ ɐ sɐʍ ʇɐɥʇ 'uɐw ɥo 'uɐW                                                                            
„noʎ llᴉʞ ɐw,I 'qɐℲ ʎǝH„ 'ʎɐp ʇxǝu ʎɹǝʌ ǝɥʇ 'uoᴉʇɐʇs oᴉpɐɹ ǝɥʇ oʇ ʇɥƃᴉɐɹʇs ʇuǝʍ ſ ʎɐᴚ oS                                             
(pɐℲ ˙ſ˙ſ) pǝǝds ɔᴉuosɹǝdns ʇɐ noʎ ʇɐ ,uᴉwoɔ sɔᴉɹʎ⅂                                                                                  
uɐwnɥ ɐ w,I ,uᴉwnssɐ noʎ 'ɐwnl-ɐwoop 'ɐwnl-ɐwns 'ɥ∩                                                                               
uɐwnɥɹǝdns w,I ¿noʎ oʇ ɥƃnoɹɥʇ ʇᴉ ʇǝƃ oʇ op ɐʇʇoƃ I ʇɐɥM                                                                             
puɐ noʎ oʇ ǝnlƃ ll,ʇᴉ puɐ 'ǝw ɟo ɟɟo ,uᴉʇǝɥɔoɔᴉɹ sᴉ ʎɐs noʎ ,uᴉɥʇʎuɐ ʇɐɥʇ os ɹǝqqnɹ ɟo ǝpɐw w,I puɐ ǝʌᴉʇɐʌouuI                       
,uᴉʇɐʇᴉʌǝl s,ʇᴉ ǝʞᴉl ,uᴉlǝǝɟ ɐ ǝɔuǝᴉpnɐ -ɹǝɥʇow ɐ ǝʌᴉƃ oʇ ʍoɥ ',uᴉʇɐɹʇsuowǝp ɹǝʌǝ uɐɥʇ ǝɹow ',uᴉʇɐʇsɐʌǝp w,I                         
,uᴉʇɐɹqǝlǝɔ ǝq ll,ʎǝɥʇ 'ɟɟo llǝɟ I ʎɐs uɐɔ ʎǝɥʇ ʇɐɥʇ ʎɐp ǝɥʇ ɹoɟ ,uᴉʇᴉɐʍ ɹǝʌǝɹoɟ ǝɹɐ sɹǝʇɐɥ ǝɥʇ ʍouʞ I puɐ ,uᴉpɐɟ ɹǝʌǝᴎ              
ɔᴉsnw ɹoʇɐʌǝlǝ ǝʞɐw noʎ 'ɔᴉsnw ,uᴉʇɐʌǝlǝ ǝʞɐw I 'pǝʇɐʌᴉʇow wǝ, ʇǝƃ oʇ ʎɐʍ ǝɥʇ ʍouʞ I ǝsnɐↃ,                                          
ʇᴉ ǝsnɟuoɔ ʎǝɥʇ 'snolɐǝɾ ʇǝƃ ʎǝɥʇ uǝɥʍ op ʎǝɥʇ ʇɐɥʍ s,ʇɐɥʇ 'llǝʍ '„wɐǝɹʇsuᴉɐw ooʇ s,ǝɥ 'ɥO„                                          
ʇᴉ ǝsnɟ oʇ ʎɐʍ ɐllǝɥ ɐ punoɟ I ǝsnɐɔ, „dod s,ʇᴉ 'doɥ-dᴉɥ ʇou s,ʇI„                                                                   
ʇᴉ ǝsol wǝ, ǝʞɐw puɐ „ɟlǝsɹno⅄ ǝso⅂„ uo ʍoɹɥʇ 'ɔoᗡ ɥʇᴉʍ dɐɹ ʞɔoɥs 'ʞɔoɹ ɥʇᴉM                                                         
„ǝsn oʇ spɹoʍ ʇɐɥʍ ʍouʞ ʇ,uop I 'ʇɐɥʇ ǝʞᴉl sƃuos ǝʞɐw oʇ ʍoɥ ʍouʞ ʇ,uop I„                                                           
noʎ snsɹǝʌ ʇɐɥʇ sǝsɹǝʌ ǝsǝɥʇ ɟo ǝuo ʎuɐ ,uᴉddᴉɹ w,I ǝlᴉɥʍ noʎ oʇ sɹnɔɔo ʇᴉ uǝɥʍ ʍouʞ ǝw ʇǝ⅂                                          
oʇ ɹǝpɹnw ɐʇʇoƃ I sǝsɹǝʌ ʎuɐw ʍoɥ 'noʎ ,uᴉʇɹnɥ ʎlʇuǝʇɹǝʌpɐuᴉ w,I 'suᴉɐʇɹnɔ s,ʇI                                                      
¿ooʇ suᴉƃɹᴉʌ ǝɔᴉɟᴉɹɔɐs plnoɔ noʎ 'sƃuos ɹnoʎ 'ǝɔᴉu sɐ ɟlɐɥ ǝɹǝʍ noʎ ɟᴉ ʇɐɥʇ ǝʌoɹԀ                                                    
ǝw ƃunɹq sllᴉʞs ǝsǝɥʇ sǝpɐloɔɔɐ ǝɥʇ ʇɐ ʞool ʇnq 'ǝᴉʞunɾ llᴉd 'ʎʞunlɟ looɥɔs 'ɥƃ∩                                                     
ʎɹƃunɥ llᴉʇs ʇnq 'ɟlǝsʎw ɟo llnℲ                                                                                                     
oʇ puᴉw ʎw ʇnd I ʇɐɥʍ op ǝw ǝʞɐw I ǝsnɐɔ, ɟlǝsʎw ʎllnq I                                                                             
sǝnƃuoʇ uᴉ ʞɐǝds I uǝɥʍ llᴉ 'noʎ ǝʌoqɐ sǝnƃɐǝl uoᴉllᴉw ɐ w,I pu∀                                                                     
noʎ -ɟ 'ʞǝǝɥɔ-uᴉ-ǝnƃuoʇ llᴉʇs s,ʇᴉ ʇnB                                                                                               
ʇɐǝs ʇuoɹɟ ǝɥʇ uᴉ dǝǝls ɐw,I 'lǝǝɥʍ -ɟ ǝɥʇ ǝʞɐʇ 'uɐʇɐS 'os 'ʞunɹp w,I                                                                
„ʎʞunℲ ʇnq ʎʞunɥↃ„ llᴉʇs 'zʎoB ǝɥʇ puɐ ᗡ ʎʌɐǝH ,uᴉdwnB                                                                               
,uᴉlƃƃnɹʇs puɐ ,uᴉƃƃnʇ lǝǝɟ uɐɔ I ,uᴉɥʇǝwos s,ǝɹǝɥʇ pɐǝɥ ʎw uᴉ ʇnB                                                                   
ǝw woɹɟ ʇuɐʍ ʎǝɥʇ ʇɐɥʍ s,ǝɹǝɥ puɐ slᴉʌǝp ɥʇᴉʍ ʇɥƃᴉɟ slǝƃu∀                                                                           
ǝʇɐɥ uǝwoʍ ǝɥʇ ɟo ǝwos ǝʇɐuᴉwᴉlǝ oʇ ǝw ,uᴉʞsɐ ǝɹ,ʎǝɥ⊥                                                                                
pǝɹʇɐɥ ɹǝʇʇᴉq ǝɥʇ uoᴉʇɐɹǝpᴉsuoɔ oʇuᴉ ǝʞɐʇ noʎ ɟᴉ ʇnB                                                                                 
uoᴉʇɐnʇᴉs ǝɥʇ oʇ ɔᴉʇǝɥʇɐdwʎs ǝɹow puɐ 'ʇuǝᴉʇɐd ǝlʇʇᴉl ɐ ǝq ʎɐw noʎ uǝɥʇ 'ǝʌɐɥ I                                                      
uoᴉʇɐuᴉwᴉɹɔsᴉp ǝɥʇ puɐʇsɹǝpun pu∀                                                                                                    
uǝɥʇ ǝpɐuowǝl ǝʞɐW ¿suowǝl noʎ ,uᴉpuɐɥ s,ǝɟᴉl 'ʇᴉ ʞɔn- ʇnB                                                                           
uǝwoʍ ǝɥʇ ɹǝʇʇɐq ʇ,uɐɔ I ɟᴉ ʇnB                                                                                                      
¿uǝɥʇ 'ǝʞɐɔ ɐ wǝ, ǝʞɐq oʇ pǝsoddns I wɐ -nɟ ǝɥʇ ʍoH                                                                                  
uɐʇɐS ɹoɟ wᴉɥ ǝʞɐʇsᴉw ʇ,uoᗡ                                                                                                          
uoᴉʇɐɔɐʌ ɐ ǝʞɐʇ puɐ sɐǝsɹǝʌo ǝq oʇ pǝǝu I ʞuᴉɥʇ noʎ ɟᴉ ǝʞɐʇsᴉw lɐʇɐɟ ɐ s,ʇI                                                          
puɐ ǝɔɐɟ ɹǝɥ uo llɐɟ ɹǝɥ ǝʞɐw puɐ 'pɐoɹq ɐ dᴉɹʇ o⊥                                                                                   
sƃuᴉlǝǝɟ ɹnoʎ ʇɹnɥ oʇ ʇou noʎ uo ʎsɐǝ oƃ ɐuuoƃ sɐʍ I 'ʞoo⅂¿po⅁ ɐ ǝq uɐɔ noʎ uǝɥʍ ƃuᴉʞ ɐ ǝq ʎɥʍ 'ʇou ʞuᴉɥ⊥ ¿ƃuᴉʞ ɐ ǝq 'pɹɐ- ɐ ǝq ʇ,uoᗡ
(sǝʇnuᴉw xᴉs 'sǝʇnuᴉw xᴉs) ǝɔuɐɥɔ ǝuo sᴉɥʇ ʇǝƃ oʇ ,uᴉoƃ ʎluo w,I ʇnB                                                                 
(uo ǝɹ,noʎ 'ʎpɐɥS wᴉlS 'sǝʇnuᴉw xᴉs) ʇᴉ lǝǝɟ uɐɔ I 'ƃuoɹʍ s,ƃuᴉɥʇǝwoS                                                                
(sǝʇnuᴉw xᴉs 'xᴉs 'sǝʇnuᴉw xᴉs) ʇɐɥʍ ʍouʞ ʇ,uop I ʇnq 'uǝddɐɥ oʇ ʇnoqɐ s,ƃuᴉɥʇǝwos ǝʞᴉl 'ʇoƃ ǝʌ,I ,uᴉlǝǝɟ ɐ ʇsnſ                     
ǝlqnoɹʇ ƃᴉq 'ǝlqnoɹʇ uᴉ ǝɹ,ǝʍ 'suɐǝw ʇᴉ ʞuᴉɥʇ I ʇɐɥʍ suɐǝw ʇɐɥʇ ɟI                                                                   
(pǝɹǝpɹo ɔop ǝɥʇ ʇɐɥʍ ʇsnɾ ǝɹɐ noʎ) sǝɔuɐɥɔ ʎuɐ ,uᴉʞɐʇ ʇou w,I 'ʎɐs noʎ sɐ sɐuɐuɐq sɐ sᴉ ǝɥ ɟᴉ pu∀                                   
po⅁ dɐᴚ 'po⅁ dɐᴚ ɐ ǝʞᴉl lǝǝɟ oʇ ,uᴉuuᴉƃǝq w,I                                                                                        
pou ʞɔɐq 'pou ʞɔɐq ǝɥʇ oʇ ʇuoɹɟ ǝɥʇ woɹɟ ǝldoǝd ʎw ll∀                                                                               
¿xoq dɐls 'xoq dɐls oʇ ɥƃnouǝ ƃuol ǝɹɐ swɹɐ ɹᴉǝɥʇ sʞuᴉɥʇ oɥʍ 'ʍoᴎ                                                                    
ʇoq-dɐᴚ ǝw llɐɔ os 'ʇoqoɹ ɐ ǝʞᴉl dɐɹ I pᴉɐs ʎǝɥ⊥                                                                                     
ʇǝʞɔod ʞɔɐq ʎw uᴉ doʇdɐl ɐ ʇoƃ I 'sǝuǝƃ ʎw uᴉ ǝq ʇsnw ʇᴉ ɹǝʇndwoɔ ɐ ǝʞᴉl dɐɹ oʇ ǝw ɹoɟ ʇnB                                           
ʇᴉɟoɹd dɐɹ ʇɐɥʇ woɹɟ ʇouʞ ʇɐɟ ɐ ʇoƃ 'ʇᴉ ʞɔoɔ-ɟlɐɥ I uǝɥʍ ɟɟo oƃ ll,uǝd ʎW                                                            
ǝɔᴉɟɟo uᴉ llᴉʇs sɐʍ uoʇuᴉlↃ llᴉB ǝɔuᴉs ɹǝʌǝ 'ʇᴉ ɟɟo ,uᴉllᴉʞ ɐ puɐ ,uᴉʌᴉl ɐ ǝpɐW                                                      
ʞɔɐs - sᴉɥ uo ,uᴉlǝǝɟ ʎʞsuᴉʍǝ⅂ ɐɔᴉuoW ɥʇᴉM                                                                                           
llǝɥ llɐ sɐ ʇuǝɔǝpuᴉ sɐ puɐ ǝpnɹ sɐ ʇnq 'ʇsǝuoɥ sɐ llᴉʇs ↃW uɐ w,I                                                                   
(ɥʇᴉʍ llɐ wǝ, llᴉʞ) ɔᴉloɥ-ɐ-llᴉʞs 'sǝlqɐllʎS                                                                                         
ɥɔʇɐw ,uᴉssᴉd ɐ oʇuᴉ ʇǝƃ ɐuuɐʍ ʎllɐǝɹ ʇ,uop noʎ 'doɥ-dᴉɥ ʎʇᴉddᴉɥ-ʎʇᴉddᴉp ʎʇᴉddᴉlɟ sᴉɥ⊥                                               
ʞɔɐʎ-ʎʇǝʞɔɐʎ 'dɐʎ-dɐʎ 'dɐɹɔ dɐɹ ʞɔɐdʞɔɐq ',ɔ∀ ǝɥʇ ɟo ʞɔɐq ǝɥʇ uᴉ Ↄ∀W ɐ ,uᴉʞɔɐd 'ʇɐɹq ʎʇᴉddɐɹ sᴉɥʇ ɥʇᴉM                               
ʇɐɥʇ ,uᴉɔᴉʇɔɐɹd w,I ǝlᴉɥʍ sʇunʇs ʇɐqoɹɔɐ lɐɔᴉɹʎl ǝsǝɥʇ ʇdwǝʇʇɐ I 'ǝwᴉʇ ǝwɐs ʇɔɐxǝ ǝɥʇ ʇɐ pu∀                                         
ɟlɐɥ uᴉ ʇᴉ ʞɔɐɹɔ puɐ - ɟo ǝldnoɔ ɐ ɟo ʞɔɐq ǝɥʇ ɹǝʌo ǝlqɐʇ -ɹǝɥʇow ɐ ʞɐǝɹq oʇ ǝlqɐ ǝq llᴉʇs ll,I                                      
ʇɔɐɟ ǝɥʇ ɹǝʇɟɐ ɥʇɐwɹǝʇɟ∀ oʇ pǝuƃᴉs sɐʍ I 'ɔᴉuoɹᴉ sɐʍ ʇᴉ pǝzᴉlɐǝɹ ʎluO                                                                
ʞɔɐʇʇɐ ɟo ɥʇɐɹʍ ʎw lǝǝɟ 'sqwoq-Ⅎ doɹp sᴉ op I ll∀ ¿ʍolq ʇou I plnoɔ ʍoH                                                              
pɐd ᴉxɐw ɐ s,ǝɹǝɥ 'poᴉɹǝd ǝwᴉʇ ɥƃnoɹ ɐ ,uᴉʌɐɥ ǝɹɐ sɹǝddɐᴚ                                                                            
ǝɔᴉdɹǝʇsɐw sᴉɥʇ ,uᴉʇɔnɹʇsuoɔ ʎllnɟɹǝʇsɐw w,I ǝlᴉɥʍ ʞɔɐʍ ǝɥʇ ɹoɟ pɐq ʎlsnoɹʇsɐsᴉp ʎllɐnʇɔɐ s,ʇI                                       
po⅁ dɐᴚ 'po⅁ dɐᴚ ɐ ǝʞᴉl lǝǝɟ oʇ ,uᴉuuᴉƃǝq w,I ǝsnɐↃ,                                                                                 
pou ʞɔɐq 'pou ʞɔɐq ǝɥʇ oʇ ʇuoɹɟ ǝɥʇ woɹɟ ǝldoǝd ʎw ll∀                                                                               
¿xoq dɐls 'xoq dɐls oʇ ɥƃnouǝ ƃuol ǝɹɐ swɹɐ ɹᴉǝɥʇ sʞuᴉɥʇ oɥʍ 'ʍoᴎ                                                                    
pɹɐɥ ʇɐɥʇ 'pɹɐɥ ʇɐɥʇ ʇ,uᴉɐ -ɥs sᴉɥʇ ,uᴉuᴉɐʇuᴉɐw noʎ ʍoɥs ǝw ʇǝ⅂                                                                      
ʇoƃ ǝʌɐɥ  ǝʞᴉl ʎʇᴉlɐʇɹowᴉ dɐɹ oʇ ʇǝɹɔǝs ǝɥʇ puɐ ʎǝʞ ǝɥʇ ʇuɐʍ ʎpoqʎɹǝʌƎ                                                              
ǝɔuɐɹǝqnxǝ lnɟɥʇnoʎ puɐ ǝƃɐɹ ʎldwᴉs 's,ʇuᴉɹdǝnlq ǝɥʇ lnɟɥʇnɹʇ ǝq oʇ 'llǝM                                                            
pᴉoɹǝʇsɐ uɐ ǝʞᴉl ɥʇɹɐƎ ǝɥʇ ʇᴉɥ 'ǝɔuɐsᴉnu ɐ ɹoɟ ʇooɹ oʇ sǝʌol ʎpoqʎɹǝʌƎ                                                               
(ʍǝd) ǝɔuᴉs uooW ǝɥʇ ɹoɟ ʇooɥs ʇnq ,uᴉɥʇou pᴉᗡ                                                                                       
„ǝwʎɥɹ ǝɥʇ snB„ 'oʇ ǝlɔᴉɥǝʌ ɐ sɐ ʇᴉ ǝsn I ǝsnɐɔ, ɔᴉsnw sᴉɥʇ ɥʇᴉʍ looɥɔs oʇ uǝʞɐʇ ʇǝƃ sↃW                                             
sʇuǝpnʇs ɟo llnɟ looɥɔs ʍǝu ɐ pɐǝl I ʍoᴎ                                                                                             
uǝᴚ 'ɔoᗡ ʎǝɥ 'ǝqnↃ '∀˙M˙ᴎ 'ɔɐԀᄅ 'zzɐqɐɥS wᴉʞɐ⅂ 'wᴉʞɐᴚ ɟo ʇɔnpoɹd ɐ w,I ¿ǝW                                                           
wᴉlS ʇoƃ ʎǝɥʇ 'noʎ ʞuɐɥʇ 'ʎzɐƎ 'ɐllǝ⅄                                                                                                
uoᴉʇᴉsod ɐ uᴉ ǝq puɐ dn ʍolq 'dn ʍoɹƃ ʎɐp ǝuo oʇ ɥƃnouǝ pǝɹᴉdsuI                                                                     
-ɹǝɥʇow ǝɥʇ oʇuᴉ wǝɥʇ ʇɔnpuᴉ puɐ '˙Ↄ˙W˙ᗡunᴚ ʇǝǝw o⊥                                                                                  
sǝwɐlɟ ɟo llɐq ɐ uᴉ ʇsɹnq puɐ ɥɔɹnɥɔ ǝɥʇ uᴉ ʞlɐʍ ll,I ɥƃnoɥʇ uǝʌǝ ǝwɐℲ ɟo llɐH lloᴚ puɐ ʞɔoᴚ                                         
(ǝwɐɥs) ɟo llɐʍ ǝɥʇ uo ǝwɐɟ ɟo loɥoɔlɐ ǝɥʇ sᴉ uᴉ pǝʇɔnpuᴉ ǝq ll,I ǝwɐℲ ɟo llɐH ʎluO                                                  
sǝwɐlɟ ɟo ʞɔolɟ ɐ ʞlɐʍ I lᴉʇ, ǝwɐƃ ɐ llɐ s,ʇᴉ ʞuᴉɥʇ - no⅄                                                                            
¿,uᴉʞuᴉɥʇ noʎ ǝɹɐ - ǝɥʇ uᴉ ʇɐɥʍ ǝw llǝʇ 'puɐ ʞuɐld ɐ ɟɟO                                                                             
(ɐɥɐɥ) ʎoq ,uᴉʞool 'ǝɔɐɟ ʇɥƃᴉɐɹʇs ɐ ɥʇᴉʍ ʇᴉ ʎɐs ʎlǝɹɐq uɐɔ I -ƃ os 'ʎoq ,uᴉʞool-ƃ ǝlʇʇᴉ⅂                                             
ʎoq ,uᴉʞool 'ǝɔɐld ǝʞɐʇ ,uᴉɹǝɥʇɐƃ ɥɔɹnɥɔ ɐ ,uᴉɥɔʇɐʍ ǝɹ,noʎ ǝʞᴉl ɹnɔɔo-ssɐw ɐ ,uᴉssǝuʇᴉʍ ǝɹ,no⅄                                       
ʎoq ,uᴉʞool 'ʎɐs ʎǝɥʇ llɐ s,ʇɐɥʇ '„-ƃ s,ʎoq ʇɐɥʇ 'ʎǝʌ ʎO„                                                                            
ʎoq ,uᴉʞool 'ʎɐp ʎɹǝʌǝ lǝqɐl ɹnoʎ woɹɟ „oƃ oʇ ʎɐM„ 'ɐ puɐ ʞɔɐq ǝɥʇ uo ʇɐd 'dn sqwnɥʇ ɐ ʇǝƃ no⅄                                       
ʎoq ,uᴉʞool 'ǝɹᗡ woɹɟ „ɥɐǝʎ llǝH„ 'ɐ ʇǝƃ I ¿ʎoq ,uᴉʞool 'ʎɐs noʎ ʇɐɥʍ 'ʎoq ,uᴉʞool 'ʎǝH                                              
ʎoq ,uᴉʞool 'ǝɔɐɟ ʎw ɐʇʇno ʇǝƃ '-s ɹoɟ ʎpoqou pǝʞsɐ ɹǝʌǝu 'ǝʌɐɥ I ,uᴉɥʇʎɹǝʌǝ ɹoɟ ʞɹoʍ ɐw,I                                           
ǝsnɐɔ, 'ʎoq ,uᴉʞool 'ǝɔɐd ǝwɐs ǝɥʇ ɥʇᴉʍ dn ,uᴉdǝǝʞ ɟo ǝlqɐdɐɔ ǝq ɐuuoƃ ɹǝʌǝu ǝɹ,noʎ 'ʎoq 'ʎllɐɔᴉsɐB                                  
po⅁ dɐᴚ 'po⅁ dɐᴚ ɐ ǝʞᴉl lǝǝɟ oʇ ,uᴉuuᴉƃǝq w,I                                                                                        
pou ʞɔɐq 'pou ʞɔɐq ǝɥʇ oʇ ʇuoɹɟ ǝɥʇ woɹɟ ǝldoǝd ʎw ll∀                                                                               
ᴚ∀ↃS∀ᴎ 'ᴚ∀ↃS∀ᴎ ǝw llɐɔ 'ʞɔɐɹʇ ǝɥʇ punoɹɐ ,uᴉɔɐɹ w,I ʎɐʍ ǝɥ⊥                                                                          
po⅁ ɥsɐɹ⊥ ǝʇᴉɥM ǝɥʇ 'ʞɹɐd ɹǝlᴉɐɹʇ ǝɥʇ ɟo ʇpɹɐɥuɹɐƎ ǝlɐᗡ                                                                              
pɹɐƃs∀ 'pɹɐƃs∀ 'ou 'uoʇdʎɹ⋊ s,ʇǝuɐld sᴉɥʇ 'poZ lɐɹǝuǝ⅁ ǝɹoɟǝq lǝǝu⋊                                                                  
ʇuǝʇodᴉuwo w,I 'ʇuǝpoɹ noʎ 'uᴉpO ǝq ll,I puɐ 'ɹoɥ⊥ ǝq ll,noʎ oS                                                                      
,uᴉʇoʇ w,I sqwoq ǝsǝɥʇ ɥʇᴉʍ ʎlǝʇɐᴉpǝwᴉ ',uᴉpɐolǝɹ w,I uǝɥʇ 'ɟɟo ʇǝ⅂                                                                 
uǝʞoʍ ǝq ʇou plnoɥs I pu∀                                                                                                            
-dǝǝp wow ɹnoʎ ʇoƃ I ʇnq ',uᴉʇɐolɟ ǝᴉqwoz ɐ 'pɐǝɥ ,uᴉʞlɐʇ ɐ ʇsnɾ w,I ʇnq 'pɐǝp ,uᴉʞlɐʍ ǝɥʇ w,I                                       
ǝlpood 'uowoɔ uᴉ ,uᴉɥʇou ǝʌɐɥ ǝʍ 'ǝlpooᴎ uǝwɐᴚ ʎw ʇno w,I                                                                           
lᴉdnd 'ǝƃɐwoɥ ʎɐd puɐ wɹɐ ǝɥʇ uᴉ ɟlǝsɹnoʎ ɥɔuᴉd 'uɐwɹǝqoᗡ ɐ w,I                                                                      
lɐʇnɹq s,ʎʇsǝuoɥ ʎw 'ǝw s,ʇI                                                                                                         
ɥƃnoɥʇ op I ʇɐɥʍ ǝzᴉlᴉʇn ʇ,uop I ɟᴉ ǝlᴉʇnɟ ʎlʇsǝuoɥ s,ʇᴉ ʇnB                                                                         
ǝlᴉɥʍ ɐ uᴉ ǝɔuo ʇsɐǝl ʇɐ 'pooƃ ɹoℲ                                                                                                   
sǝwʎɥɹ ɥƃnouǝ ǝlpoop puɐ ǝlqqᴉɹɔs I ɥɔʇɐɹɔs uǝʞɔᴉɥɔ sᴉɥʇ uᴉ ǝɹǝɥʍǝwos ǝɹns ǝʞɐw ɐuuɐʍ I oS                                           
sǝwᴉʇ ɥƃnoʇ ɥƃnoɹɥʇ ǝldoǝd ǝwos ʇǝƃ dlǝɥ oʇ ʎɹʇ ǝqʎɐw o⊥                                                                             
pǝuƃᴉsun noʎ uǝʌǝ ǝsnɐɔ, ǝsɐɔ uᴉ ʇsnɾ sǝuᴉlɥɔund ʍǝɟ ɐ dǝǝʞ ɐʇʇoƃ I ʇnB                                                              
ǝwᴉʇɥɔunl s,ʇᴉ ǝʞᴉl ǝw ʇɐ ,uᴉʞool ʎɹƃunɥ ǝɹɐ sɹǝddɐᴚ                                                                                 
punoɹƃɹǝpun ǝɥʇ ɟo ƃuᴉʞ sɐʍ I ǝɔuo ǝɹǝɥʍ ǝwᴉʇ ɐ sɐʍ ǝɹǝɥʇ ʍouʞ I                                                                     
puᴉɹƃ ɥɔuoW ǝɥɐoɹɐɥԀ ʎw uo w,I ǝʞᴉl dɐɹ llᴉʇs I ʇnB                                                                                  
ǝuᴉqwoɔ noʎ uǝɥʍ sǝwᴉʇǝwos ʇnq 'sǝwʎɥɹ ɥɔunɹɔ I oS                                                                                   
ǝuᴉw ɟo ɹoloɔ uᴉʞs ǝɥʇ ɥʇᴉʍ lɐǝdd∀                                                                                                   
ǝuᴉl ǝuo ʇɐɥʇ ǝʞᴉl noʎ ɹosuǝɔ oʇ ,uᴉʎɹʇ ǝwoɔ ʎǝɥʇ ǝɹǝɥ puɐ ƃᴉq ooʇ ʇǝƃ no⅄                                                           
ǝuᴉqwnloↃ woɹɟ -ʞ uǝʌǝs ǝʞɐʇ ll,I ʎɐs oʇ pǝᴉɹʇ I uǝɥʍ Ɩ Ԁ⅂ sɹǝɥʇɐW ǝɥ⊥ woɹɟ „ʞɔɐB w,I„ 'uo pᴉɐs I                                    
6˙ ɐ puɐ ɹǝʌloʌǝɹ ɐ 'Ɫᔭ-⋊∀ uɐ ppɐ 'ǝuᴉl ɐ uᴉ llɐ wǝ, ʇnԀ                                                                             
w,I ʇnq 'sɐʍ I sɐ ƃᴉq sɐ ʇ,uᴉɐ I ʇɐɥʇ ʍou ʇᴉ ɥʇᴉʍ ʎɐʍɐ ʇǝƃ I ɟᴉ ǝǝS                                                                  
lɐʇɹod ǝɥʇ ɥƃnoɹɥʇ ,uᴉwoɔ 'lɐʇɹowᴉ uɐ oʇuᴉ ,uᴉɥdɹoW                                                                                 
ɥƃnoɥʇ ᔭ00ᄅ woɹɟ dɹɐʍ ǝwᴉʇ ɐ uᴉ ʞɔnʇs ǝɹ,no⅄                                                                                         
ɹoɟ ǝwʎɥɹ noʎ ʇɐɥʇ -ɟ ǝɥʇ ʇɐɥʍ ʍouʞ ʇ,uop I pu∀                                                                                      
sʍoɹuɹoɔ ,uᴉʞɔ- ɥʇᴉʍ lǝzundɐᴚ sɐ ssǝlʇuᴉod ǝɹ,no⅄                                                                                    
lɐwɹou ,uᴉǝq -Ⅎ ¿lɐwɹou ǝʇᴉɹʍ no⅄                                                                                                    
ǝɹnʇnɟ ǝɥʇ woɹɟ unƃʎɐɹ ʍǝu ɐ ʇɥƃnoq ʇsnɾ I pu∀                                                                                       
pɐw ſ ʎɐᴚ ǝpɐw snoloqɐℲ uǝɥʍ ǝʞᴉl 'ɐʎ ʇooɥs puɐ ǝwoɔ oʇ ʇsnſ                                                                         
ouɐᴉd pǝʎɐld ǝɥ ǝlᴉɥʍ uɐw ɐ oʇ ,uᴉƃuᴉs pɐd s,ɹǝɥʇɐǝʍʎɐW ʇɐ - ɐ ǝʞᴉl pǝʞool ǝɥ pᴉɐs qɐℲ ǝsnɐↃ,                                        
lǝuuɐɥɔ ǝlqɐɔ ǝɥʇ uo lɐᴉɔǝds Ɫ-ᔭᄅ ɐ sɐʍ ʇɐɥʇ 'uɐw ɥo 'uɐW                                                                            
„noʎ llᴉʞ ɐw,I 'qɐℲ ʎǝH„ 'ʎɐp ʇxǝu ʎɹǝʌ ǝɥʇ 'uoᴉʇɐʇs oᴉpɐɹ ǝɥʇ oʇ ʇɥƃᴉɐɹʇs ʇuǝʍ ſ ʎɐᴚ oS                                             
(pɐℲ ˙ſ˙ſ) pǝǝds ɔᴉuosɹǝdns ʇɐ noʎ ʇɐ ,uᴉwoɔ sɔᴉɹʎ⅂                                                                                  
uɐwnɥ ɐ w,I ,uᴉwnssɐ noʎ 'ɐwnl-ɐwoop 'ɐwnl-ɐwns 'ɥ∩                                                                               
uɐwnɥɹǝdns w,I ¿noʎ oʇ ɥƃnoɹɥʇ ʇᴉ ʇǝƃ oʇ op ɐʇʇoƃ I ʇɐɥM                                                                             
puɐ noʎ oʇ ǝnlƃ ll,ʇᴉ puɐ 'ǝw ɟo ɟɟo ,uᴉʇǝɥɔoɔᴉɹ sᴉ ʎɐs noʎ ,uᴉɥʇʎuɐ ʇɐɥʇ os ɹǝqqnɹ ɟo ǝpɐw w,I puɐ ǝʌᴉʇɐʌouuI                       
,uᴉʇɐʇᴉʌǝl s,ʇᴉ ǝʞᴉl ,uᴉlǝǝɟ ɐ ǝɔuǝᴉpnɐ -ɹǝɥʇow ɐ ǝʌᴉƃ oʇ ʍoɥ ',uᴉʇɐɹʇsuowǝp ɹǝʌǝ uɐɥʇ ǝɹow ',uᴉʇɐʇsɐʌǝp w,I                         
,uᴉʇɐɹqǝlǝɔ ǝq ll,ʎǝɥʇ 'ɟɟo llǝɟ I ʎɐs uɐɔ ʎǝɥʇ ʇɐɥʇ ʎɐp ǝɥʇ ɹoɟ ,uᴉʇᴉɐʍ ɹǝʌǝɹoɟ ǝɹɐ sɹǝʇɐɥ ǝɥʇ ʍouʞ I puɐ ,uᴉpɐɟ ɹǝʌǝᴎ              
ɔᴉsnw ɹoʇɐʌǝlǝ ǝʞɐw noʎ 'ɔᴉsnw ,uᴉʇɐʌǝlǝ ǝʞɐw I 'pǝʇɐʌᴉʇow wǝ, ʇǝƃ oʇ ʎɐʍ ǝɥʇ ʍouʞ I ǝsnɐↃ,                                          
ʇᴉ ǝsnɟuoɔ ʎǝɥʇ 'snolɐǝɾ ʇǝƃ ʎǝɥʇ uǝɥʍ op ʎǝɥʇ ʇɐɥʍ s,ʇɐɥʇ 'llǝʍ '„wɐǝɹʇsuᴉɐw ooʇ s,ǝɥ 'ɥO„                                          
ʇᴉ ǝsnɟ oʇ ʎɐʍ ɐllǝɥ ɐ punoɟ I ǝsnɐɔ, „dod s,ʇᴉ 'doɥ-dᴉɥ ʇou s,ʇI„                                                                   
ʇᴉ ǝsol wǝ, ǝʞɐw puɐ „ɟlǝsɹno⅄ ǝso⅂„ uo ʍoɹɥʇ 'ɔoᗡ ɥʇᴉʍ dɐɹ ʞɔoɥs 'ʞɔoɹ ɥʇᴉM                                                         
„ǝsn oʇ spɹoʍ ʇɐɥʍ ʍouʞ ʇ,uop I 'ʇɐɥʇ ǝʞᴉl sƃuos ǝʞɐw oʇ ʍoɥ ʍouʞ ʇ,uop I„                                                           
noʎ snsɹǝʌ ʇɐɥʇ sǝsɹǝʌ ǝsǝɥʇ ɟo ǝuo ʎuɐ ,uᴉddᴉɹ w,I ǝlᴉɥʍ noʎ oʇ sɹnɔɔo ʇᴉ uǝɥʍ ʍouʞ ǝw ʇǝ⅂                                          
oʇ ɹǝpɹnw ɐʇʇoƃ I sǝsɹǝʌ ʎuɐw ʍoɥ 'noʎ ,uᴉʇɹnɥ ʎlʇuǝʇɹǝʌpɐuᴉ w,I 'suᴉɐʇɹnɔ s,ʇI                                                      
¿ooʇ suᴉƃɹᴉʌ ǝɔᴉɟᴉɹɔɐs plnoɔ noʎ 'sƃuos ɹnoʎ 'ǝɔᴉu sɐ ɟlɐɥ ǝɹǝʍ noʎ ɟᴉ ʇɐɥʇ ǝʌoɹԀ                                                    
ǝw ƃunɹq sllᴉʞs ǝsǝɥʇ sǝpɐloɔɔɐ ǝɥʇ ʇɐ ʞool ʇnq 'ǝᴉʞunɾ llᴉd 'ʎʞunlɟ looɥɔs 'ɥƃ∩                                                     
ʎɹƃunɥ llᴉʇs ʇnq 'ɟlǝsʎw ɟo llnℲ                                                                                                     
oʇ puᴉw ʎw ʇnd I ʇɐɥʍ op ǝw ǝʞɐw I ǝsnɐɔ, ɟlǝsʎw ʎllnq I                                                                             
sǝnƃuoʇ uᴉ ʞɐǝds I uǝɥʍ llᴉ 'noʎ ǝʌoqɐ sǝnƃɐǝl uoᴉllᴉw ɐ w,I pu∀                                                                     
noʎ -ɟ 'ʞǝǝɥɔ-uᴉ-ǝnƃuoʇ llᴉʇs s,ʇᴉ ʇnB                                                                                               
ʇɐǝs ʇuoɹɟ ǝɥʇ uᴉ dǝǝls ɐw,I 'lǝǝɥʍ -ɟ ǝɥʇ ǝʞɐʇ 'uɐʇɐS 'os 'ʞunɹp w,I                                                                
„ʎʞunℲ ʇnq ʎʞunɥↃ„ llᴉʇs 'zʎoB ǝɥʇ puɐ ᗡ ʎʌɐǝH ,uᴉdwnB                                                                               
,uᴉlƃƃnɹʇs puɐ ,uᴉƃƃnʇ lǝǝɟ uɐɔ I ,uᴉɥʇǝwos s,ǝɹǝɥʇ pɐǝɥ ʎw uᴉ ʇnB                                                                   
ǝw woɹɟ ʇuɐʍ ʎǝɥʇ ʇɐɥʍ s,ǝɹǝɥ puɐ slᴉʌǝp ɥʇᴉʍ ʇɥƃᴉɟ slǝƃu∀                                                                           
ǝʇɐɥ uǝwoʍ ǝɥʇ ɟo ǝwos ǝʇɐuᴉwᴉlǝ oʇ ǝw ,uᴉʞsɐ ǝɹ,ʎǝɥ⊥                                                                                
pǝɹʇɐɥ ɹǝʇʇᴉq ǝɥʇ uoᴉʇɐɹǝpᴉsuoɔ oʇuᴉ ǝʞɐʇ noʎ ɟᴉ ʇnB                                                                                 
uoᴉʇɐnʇᴉs ǝɥʇ oʇ ɔᴉʇǝɥʇɐdwʎs ǝɹow puɐ 'ʇuǝᴉʇɐd ǝlʇʇᴉl ɐ ǝq ʎɐw noʎ uǝɥʇ 'ǝʌɐɥ I                                                      
uoᴉʇɐuᴉwᴉɹɔsᴉp ǝɥʇ puɐʇsɹǝpun pu∀                                                                                                    
uǝɥʇ ǝpɐuowǝl ǝʞɐW ¿suowǝl noʎ ,uᴉpuɐɥ s,ǝɟᴉl 'ʇᴉ ʞɔn- ʇnB                                                                           
uǝwoʍ ǝɥʇ ɹǝʇʇɐq ʇ,uɐɔ I ɟᴉ ʇnB                                                                                                      
¿uǝɥʇ 'ǝʞɐɔ ɐ wǝ, ǝʞɐq oʇ pǝsoddns I wɐ -nɟ ǝɥʇ ʍoH                                                                                  
uɐʇɐS ɹoɟ wᴉɥ ǝʞɐʇsᴉw ʇ,uoᗡ                                                                                                          
uoᴉʇɐɔɐʌ ɐ ǝʞɐʇ puɐ sɐǝsɹǝʌo ǝq oʇ pǝǝu I ʞuᴉɥʇ noʎ ɟᴉ ǝʞɐʇsᴉw lɐʇɐɟ ɐ s,ʇI                                                          
puɐ ǝɔɐɟ ɹǝɥ uo llɐɟ ɹǝɥ ǝʞɐw puɐ 'pɐoɹq ɐ dᴉɹʇ o⊥                                                                                   
¿po⅁ ɐ ǝq uɐɔ noʎ uǝɥʍ ƃuᴉʞ ɐ ǝq ʎɥʍ 'ʇou ʞuᴉɥ⊥ ¿ƃuᴉʞ ɐ ǝq 'pɹɐ- ɐ ǝq ʇ,uoᗡ                                                          
""")