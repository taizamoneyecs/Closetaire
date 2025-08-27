import { Tabs } from 'expo-router';
import { Text } from 'react-native';

export default function TabLayout() {
  return (
    <Tabs>
      <Tabs.Screen 
        name="index" 
        options={{ 
          title: 'Chat',
          tabBarIcon: ({ color }) => <Text>💬</Text>
        }} 
      />
      <Tabs.Screen 
        name="closet" 
        options={{ 
          title: 'Closet',
          tabBarIcon: ({ color }) => <Text>👕</Text>
        }} 
      />
    </Tabs>
  );
}