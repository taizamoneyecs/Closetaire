import { FlatList, Image, View } from 'react-native';

const ClosetGrid = () => {
  //replace with real data later
  const closetItems = [
    { id: 1, image: 'https://placehold.co/150x200/FFB6C1/white?text=Summer+Dress' },
    { id: 2, image: 'https://placehold.co/150x200/ADD8E6/white?text=Denim+Jacket' },
    { id: 3, image: 'https://placehold.co/150x200/90EE90/white?text=Wedding+Suit' },
  ];

  return (
    <FlatList
      data={closetItems}
      numColumns={2}
      renderItem={({ item }) => (
        <View style={{ margin: 10 }}>
          <Image
            source={{ uri: item.image }}
            style={{ width: 150, height: 200, borderRadius: 10 }}
          />
        </View>
      )}
    />
  );
};

export default ClosetGrid;