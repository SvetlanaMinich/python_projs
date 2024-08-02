# from transformers import pipeline

# clf = pipeline(task='text-classification',
#                model='SkolkovoInstitute/russian_toxicity_classifier')

# text = ['У нас в есть убунты и текникал превью.',
#     	'Как минимум два малолетних дегенерата в треде, мда.']

# print(clf(text))


# import torch
# import requests
# from PIL import Image
# from io import BytesIO
# from transformers import AutoImageProcessor, AutoModelForImageClassification


# IMAGE IS NOT CORRECT
# response = requests.get('https://yandex.by/images/search?from=tabbar&img_url=https%3A%2F%2Fscontent-hel3-1.cdninstagram.com%2Fv%2Ft51.2885-15%2F18723511_1899225616999921_7730884619620319232_n.jpg%3Fstp%3Dc0.80.640.640a_dst-jpg_e35%26_nc_ht%3Dscontent-hel3-1.cdninstagram.com%26_nc_cat%3D101%26_nc_ohc%3DWZPh_uKOPh8AX9VCXW_%26edm%3DAOQ1c0wBAAAA%26ccb%3D7-5%26oh%3D00_AfDjtX7hnMqWnm86fSthwly-nyKt5yF_wtNh6ZFbDyYQxw%26oe%3D65DDCD78%26_nc_sid%3D8b3546&pos=34&rpt=simage&text=cat%20jpg')
# img = Image.open(BytesIO(response.content))

# img_proc = AutoImageProcessor.from_pretrained('google/vit-base-patch16-224')
# model = AutoModelForImageClassification.from_pretrained('google/vit-base-patch16-224')

# inputs = img_proc(img, return_tensors='pt')

# with torch.no_grad():
#     logits = model(**inputs).logits

# predicted_id = logits.argmax(-1).item()
# predicted_lable = model.config.id2label[predicted_id]

# print(predicted_id, '-', predicted_lable)


#