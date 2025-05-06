import os
import tensorflow as tf
from tensorflow.keras.preprocessing.image import ImageDataGenerator
from tensorflow.keras.applications import MobileNetV2
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense, GlobalAveragePooling2D, Dropout
from tensorflow.keras.optimizers import Adam



base_dir = 'data_set'
fruit_dir = os.path.join(base_dir, 'Fruits')
veg_dir = os.path.join(base_dir, 'Vegetables')


# fruit_classes = ['FreshApple', 'RottenApple', 'FreshBanana', 'RottenBanana', 'FreshMango', 'RottenMango', 'FreshSweetMelon' ,'FreshWaterMelon',
#                'FreshOrange', 'RottenOrange', 'FreshStrawberry', 'RottenStrawberry', 'FreshCarrot', 'RottenCarrot', 'RottenSweetmelon','RottenWaterMelon',
#                'FreshTomato', 'RottenTomato', 'FreshCucumber', 'RottenCucumber', 'FreshPotato', 'RottenPotato', 
#                'FreshBellpepper', 'RottenBellpepper' , 'FreshSpinach' , 'FreshOninon' , 'Freshchili' , 'FreshGuva' ,'FreshBeetroot' ,'FreshSapota' ,'freshCauliflower']

# veg_classes = ['FreshApple', 'RottenApple', 'FreshBanana', 'RottenBanana', 'FreshMango', 'RottenMango', 'FreshSweetMelon' ,'FreshWaterMelon',
#                'FreshOrange', 'RottenOrange', 'FreshStrawberry', 'RottenStrawberry', 'FreshCarrot', 'RottenCarrot', 'RottenSweetmelon','RottenWaterMelon',
#                'FreshTomato', 'RottenTomato', 'FreshCucumber', 'RottenCucumber', 'FreshPotato', 'RottenPotato', 
#                'FreshBellpepper', 'RottenBellpepper' , 'FreshSpinach' , 'FreshOninon' , 'Freshchili' , 'FreshGuva' ,'FreshBeetroot' ,'FreshSapota' ,'freshCauliflower' ,'FreshBellpaper' ,'RottenBellpaper']


all_classes = fruit_classes + veg_classes


train_datagen = ImageDataGenerator(
    rescale=1./255,
    shear_range=0.2,
    zoom_range=0.2,
    horizontal_flip=True,
    validation_split=0.2
)


train_generator = train_datagen.flow_from_directory(
    base_dir,
    target_size=(150, 150),
    batch_size=32,
    classes=all_classes,
    class_mode='categorical',
    subset='training'
)


validation_generator = train_datagen.flow_from_directory(
    base_dir,
    target_size=(150, 150),
    batch_size=32,
    classes=all_classes,
    class_mode='categorical',
    subset='validation'
)

base_model = MobileNetV2(weights='imagenet', include_top=False, input_shape=(150, 150, 3))


base_model.trainable = False

model = Sequential([
    base_model,
    GlobalAveragePooling2D(),
    Dropout(0.5),
    Dense(128, activation='relu'),
    Dropout(0.5),
    Dense(len(all_classes), activation='softmax')  # Number of classes
])


model.compile(optimizer=Adam(learning_rate=0.001), loss='categorical_crossentropy', metrics=['accuracy'])

print("Train the model")

history = model.fit(
    train_generator,
    steps_per_epoch=train_generator.samples // train_generator.batch_size,
    validation_data=validation_generator,
    validation_steps=validation_generator.samples // validation_generator.batch_size,
    epochs=10
)


print("Save the combined model")

model.save('fruit_veg_freshness_model.h5')