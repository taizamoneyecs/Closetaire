import { createBottomTabNavigator } from '@react-navigation/bottom-tabs';
import { NavigationContainer } from '@react-navigation/native';
import { useState } from 'react';
import { FlatList, Text, TextInput, View } from 'react-native';

// 1. Create the tab navigator
const Tab = createBottomTabNavigator();

// 2. Your existing chat screen code (as a separate component)
function ChatScreen() {
  const [messages, setMessages] = useState([
    { id: 1, text: "Hello, I am your personal shopper. How can I assist you today?", fromUser: false }
  ]);
  const [inputText, setInputText] = useState('');

  const handleSend = () => {
    if (inputText.trim()) {
      setMessages(prev => [...prev, { id: Date.now(), text: inputText, fromUser: true }]);
      
      setTimeout(() => {
        setMessages(prev => [...prev, { 
          id: Date.now(), 
          text: "I understand you're looking for wedding outfits. Let me suggest something...", 
          fromUser: false 
        }]);
      }, 1000);
      
      setInputText('');
    }
  };

  return (
    <View style={{ flex: 1, padding: 20 }}>
      <FlatList
        data={messages}
        renderItem={({ item }) => (
          <View style={{ 
            alignSelf: item.fromUser ? 'flex-end' : 'flex-start',
            backgroundColor: item.fromUser ? '#007AFF' : '#E5E5EA',
            padding: 10,
            borderRadius: 20,
            marginVertical: 5
          }}>
            <Text style={{ color: item.fromUser ? 'white' : 'black' }}>
              {item.text}
            </Text>
          </View>
        )}
      />
      
      <TextInput
        value={inputText}
        onChangeText={setInputText}
        placeholder="Tell me about your event..."
        onSubmitEditing={handleSend}
        style={{ 
          borderWidth: 1, 
          borderColor: '#CCC', 
          borderRadius: 25, 
          padding: 15, 
          marginTop: 10 
        }}
      />
    </View>
  );
}

// 3. Simple closet screen (you'll improve this later)
function ClosetScreen() {
  return (
    <View style={{ flex: 1, justifyContent: 'center', alignItems: 'center' }}>
      <Text>Your virtual closet will go here!</Text>
    </View>
  );
}

// 4. Main app with navigation
export default function App() {
  return (
    <NavigationContainer>
      <Tab.Navigator>
        <Tab.Screen name="Chat" component={ChatScreen} />
        <Tab.Screen name="Closet" component={ClosetScreen} />
      </Tab.Navigator>
    </NavigationContainer>
  );
}