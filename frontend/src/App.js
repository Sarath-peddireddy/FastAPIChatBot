import React, { useState } from 'react';
import {
  Container,
  TextField,
  Button,
  Paper,
  Typography,
  Box,
  CircularProgress,
  Table,
  TableBody,
  TableCell,
  TableContainer,
  TableHead,
  TableRow,
} from '@mui/material';
import axios from 'axios';

function App() {
  const [query, setQuery] = useState('');
  const [loading, setLoading] = useState(false);
  const [results, setResults] = useState(null);
  const [error, setError] = useState(null);

  const handleSubmit = async (e) => {
    e.preventDefault();
    setLoading(true);
    setError(null);
    setResults(null);

    try {
      const response = await axios.post('http://localhost:8000/api/query', {
        query: query
      });
      setResults(response.data);
    } catch (err) {
      setError(err.response?.data?.detail || 'An error occurred');
    } finally {
      setLoading(false);
    }
  };

  return (
    <Container maxWidth="md" sx={{ py: 4 }}>
      <Typography variant="h4" component="h1" gutterBottom align="center">
        LLM-Powered Customer Query System
      </Typography>

      <Paper elevation={3} sx={{ p: 3, mb: 3 }}>
        <form onSubmit={handleSubmit}>
          <TextField
            fullWidth
            label="Enter your query"
            value={query}
            onChange={(e) => setQuery(e.target.value)}
            placeholder="Example: Show me all female customers from Mumbai"
            margin="normal"
            variant="outlined"
          />
          <Box sx={{ mt: 2, display: 'flex', justifyContent: 'center' }}>
            <Button
              type="submit"
              variant="contained"
              color="primary"
              disabled={loading || !query.trim()}
              sx={{ minWidth: 120 }}
            >
              {loading ? <CircularProgress size={24} /> : 'Submit Query'}
            </Button>
          </Box>
        </form>
      </Paper>

      {error && (
        <Paper elevation={3} sx={{ p: 2, mb: 3, bgcolor: '#ffebee' }}>
          <Typography color="error">{error}</Typography>
        </Paper>
      )}

      {results && (
        <Paper elevation={3} sx={{ p: 3 }}>
          <Typography variant="h6" gutterBottom>
            Generated SQL Query:
          </Typography>
          <Paper elevation={1} sx={{ p: 2, mb: 3, bgcolor: '#f5f5f5' }}>
            <Typography component="pre" sx={{ fontFamily: 'monospace' }}>
              {results.sql_query}
            </Typography>
          </Paper>

          <Typography variant="h6" gutterBottom>
            Results:
          </Typography>
          <TableContainer>
            <Table>
              <TableHead>
                <TableRow>
                  {results.results[0] && Object.keys(results.results[0]).map((key) => (
                    <TableCell key={key}>{key}</TableCell>
                  ))}
                </TableRow>
              </TableHead>
              <TableBody>
                {results.results.map((row, index) => (
                  <TableRow key={index}>
                    {Object.values(row).map((value, i) => (
                      <TableCell key={i}>{value}</TableCell>
                    ))}
                  </TableRow>
                ))}
              </TableBody>
            </Table>
          </TableContainer>
        </Paper>
      )}
    </Container>
  );
}

export default App; 