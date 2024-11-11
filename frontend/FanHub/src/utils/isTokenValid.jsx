import { jwtDecode } from 'jwt-decode';


function isTokenValid(token) {
  if (!token) return false;

  try {
    const decoded = jwtDecode(token);


    if (!decoded.exp) {
      return false;
    }

    const currentTime = Date.now() / 1000; 


    return decoded.exp > currentTime;
  } catch (error) {

    return false;
  }
}

export default isTokenValid;
