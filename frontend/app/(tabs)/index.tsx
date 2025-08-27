import { useState } from 'react';
import { FlatList, Text, TextInput, View } from 'react-native';

export default function ChatScreen() {
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
