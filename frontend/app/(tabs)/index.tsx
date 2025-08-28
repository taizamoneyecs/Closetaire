import { useState } from 'react';
import { FlatList, Text, TextInput, View, Alert } from 'react-native';

export default function ChatScreen() {
  const [messages, setMessages] = useState([
    { id: 1, text: "Hello, I am your personal shopper. How can I assist you today?", fromUser: false }
  ]);
  const [inputText, setInputText] = useState('');
  const [isLoading, setIsLoading] = useState(false);

  const handleSend = async () => {
  if (inputText.trim()) {
    const userMessage = inputText.trim();

    // Add user message immediately
    setMessages(prev => [...prev, { id: Date.now(), text: userMessage, fromUser: true }]);
    setInputText('');
    setIsLoading(true);

    try {
      // Call your Python API
      const response = await fetch('http://192.168.1.165:5000/api/chat', {
        method: 'POST',
        headers: {
          'Content-Type': 'application/json',
        },
        body: JSON.stringify({
          message: userMessage
        })
      });

      const data = await response.json();
      console.log("Backend response:", data); // <-- log full backend response

      // Add AI response (with safety check)
      setMessages(prev => [...prev, {
        id: Date.now(),
        text: data.response || "Sorry, no suggestion was generated.",
        fromUser: false
      }]);

    } catch (error) {
      Alert.alert('Error', 'Could not connect to server');
      console.error('API Error:', error);
    } finally {
      setIsLoading(false);
    }
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
        placeholder={isLoading ? "Getting response..." : "Tell me about your event..."}
        onSubmitEditing={handleSend}
        editable={!isLoading}
        style={{
          borderWidth: 1,
          borderColor: '#CCC',
          borderRadius: 25,
          padding: 15,
          marginTop: 10,
          opacity: isLoading ? 0.6 : 1
        }}
      />
    </View>
  );
}