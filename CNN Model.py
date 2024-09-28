import tensorflow as tf
from tf_keras import layers, models
from tf_keras.preprocessing.image import ImageDataGenerator
from tf_keras.callbacks import EarlyStopping, ReduceLROnPlateau
import matplotlib.pyplot as plt

# Hyperparameters
learning_rate = 1e-3
num_epochs = 10
batch_size = 64
img_height = 640# Replace with your actual image height
img_width = 640 # Replace with your actual image width
num_classes = 1  # Adjust based on the number of classes (e.g., craters and boulders)

# Image Data Generator for loading data and performing real-time data augmentation
train_datagen = ImageDataGenerator(
    rescale=1./255,  # Rescale pixel values from [0, 255] to [0, 1]
    shear_range=0.2,  # Randomly apply shearing transformation
    zoom_range=0.2,  # Randomly zoom
    horizontal_flip=True,  # Randomly flip images
    validation_split=0.1  # Split for validation
)

# Load the dataset
train_gen = train_datagen.flow_from_directory(
    r'C:\Users\nandi\Desktop\Hack The Space\Dataset\train',  # Replace with the path to your train folder
    target_size=(img_height, img_width),
    batch_size=batch_size,
    class_mode='categorical',
    subset='training'  # Set as training data
)

validation_gen = train_datagen.flow_from_directory(
    r'C:\Users\nandi\Desktop\Hack The Space\Dataset\valid',  # Use the same folder, but split for validation
    target_size=(img_height, img_width),
    batch_size=batch_size,
    class_mode='categorical',
    subset='validation'  # Set as validation data
)

# Create the CNN model
def create_model():
    model = models.Sequential()
    
    # Convolutional Layer 1
    model.add(layers.Conv2D(32, (5, 5), activation='relu', input_shape=(img_height, img_width, 3)))
    model.add(layers.BatchNormalization())
    model.add(layers.MaxPooling2D(pool_size=(2, 2)))
    model.add(layers.Dropout(0.45))
    
    # Convolutional Layer 2
    model.add(layers.Conv2D(64, (5, 5), activation='relu'))
    model.add(layers.BatchNormalization())
    model.add(layers.MaxPooling2D(pool_size=(2, 2)))
    model.add(layers.Dropout(0.35))
    
     # Convolutional Layer 2
    model.add(layers.Conv2D(128, (5, 5), activation='relu'))
    model.add(layers.BatchNormalization())
    model.add(layers.MaxPooling2D(pool_size=(2, 2)))
    model.add(layers.Dropout(0.35))

    # Flatten the output
    model.add(layers.Flatten())
    
    # Fully Connected Layers
    model.add(layers.Dense(512, activation='relu'))
    model.add(layers.Dense(num_classes, activation='softmax'))
    
    return model

# Create and compile the model
model = create_model()
model.compile(optimizer=tf.keras.optimizers.legacy.Adam(learning_rate=learning_rate),
              loss='categorical_crossentropy',
              metrics=['accuracy'])

# Callbacks
early_stopping = EarlyStopping(monitor='val_loss', patience=5, restore_best_weights=True)
lr_scheduler = ReduceLROnPlateau(monitor='val_loss', factor=0.5, patience=3, min_lr=1e-6)

# Train the model
history = model.fit(train_gen, epochs=num_epochs, 
                    validation_data=validation_gen, 
                    callbacks=[early_stopping, lr_scheduler])

# Load and prepare the test dataset
test_datagen = ImageDataGenerator(rescale=1./255)


# Plot training and validation accuracy over epochs
plt.plot(history.history['accuracy'], label='Train Accuracy')
plt.plot(history.history['val_accuracy'], label='Validation Accuracy')
plt.title('Model Accuracy')
plt.xlabel('Epochs')
plt.ylabel('Accuracy')
plt.legend()
plt.show()
