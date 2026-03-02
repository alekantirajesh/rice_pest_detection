import torch
import torch.nn as nn
import torch.optim as optim
from torchvision import datasets, transforms, models
from torch.utils.data import DataLoader

def main():
    device = torch.device("cuda" if torch.cuda.is_available() else "cpu")

    # Data augmentation
    train_transforms = transforms.Compose([
        transforms.Resize((224, 224)),
        transforms.RandomHorizontalFlip(),
        transforms.RandomRotation(15),
        transforms.ColorJitter(brightness=0.2, contrast=0.2),
        transforms.ToTensor(),
    ])

    # 🔴 Your renamed dataset path
    data_dir = "ip102_rice"

    train_dataset = datasets.ImageFolder(data_dir, transform=train_transforms)
    train_loader = DataLoader(train_dataset, batch_size=8, shuffle=True, num_workers=2)

    num_classes = len(train_dataset.classes)  # should be 12

    print("Total training images:", len(train_dataset))
    print("Detected Classes:")
    for idx, name in enumerate(train_dataset.classes):
        print(f"{idx} -> {name}")

    # Load ResNet50
    model = models.resnet50(weights=None)

    # Match pretrained IP102 checkpoint (102 classes)
    model.fc = nn.Linear(model.fc.in_features, 102)

    # Load pretrained weights
    state_dict = torch.load("model.pkl", map_location=device)
    model.load_state_dict(state_dict)
    print("\n✅ Pretrained IP102 weights loaded!")

    # Replace final layer for rice pest classes (12)
    model.fc = nn.Linear(model.fc.in_features, num_classes)
    print(f"✅ Final layer replaced for {num_classes} rice pest classes")

    # Freeze backbone
    for param in model.parameters():
        param.requires_grad = False

    # Train only classifier
    for param in model.fc.parameters():
        param.requires_grad = True

    model = model.to(device)

    criterion = nn.CrossEntropyLoss()
    optimizer = optim.Adam(model.fc.parameters(), lr=0.0005)

    # Training
    epochs = 5
    for epoch in range(epochs):
        model.train()
        running_loss = 0.0

        for batch_idx, (images, labels) in enumerate(train_loader):
            images, labels = images.to(device), labels.to(device)

            optimizer.zero_grad()
            outputs = model(images)
            loss = criterion(outputs, labels)
            loss.backward()
            optimizer.step()

            running_loss += loss.item()

            if batch_idx % 20 == 0:
                print(f"Epoch {epoch+1}, Batch {batch_idx}, Loss: {loss.item():.4f}")

        print(f"\nEpoch [{epoch+1}/{epochs}] Total Loss: {running_loss:.4f}\n")

    # Save model
    torch.save({
        "model_state": model.state_dict(),
        "classes": train_dataset.classes
    }, "final_rice_pest_model.pth")

    print("🎉 Training complete! Model saved as final_rice_pest_model.pth")

if __name__ == "__main__":
    main()
