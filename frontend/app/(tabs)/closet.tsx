import { Text, View } from 'react-native';
import ClosetGrid from '../../components/ClosetGrid';

export default function ClosetScreen() {
  return (
    <View style={{ flex: 1, padding: 20 }}>
      <Text style={{ fontSize: 24, fontWeight: 'bold', marginBottom: 20 }}>
        Your Virtual Closet
      </Text>
      <ClosetGrid />
    </View>
  );
}