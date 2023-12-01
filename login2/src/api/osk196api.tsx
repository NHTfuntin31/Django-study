import axios from 'axios';
import { NavigateFunction } from 'react-router-dom';

axios.defaults.withCredentials = true;

const UserLogin = (
   username: string,
   password: string,
   handleCheckLoginSuccess?: () => void
) => {
    if (username && password) {
        const body = {
            "username": username,
            "password": password 
        }
        console.log(body);
        const apiUrl = "http://osk-196/api/login";
        axios
            .post(apiUrl, body)
            .then((res) => {
                console.log(res);
                if (handleCheckLoginSuccess) {
                    handleCheckLoginSuccess();
                }
            })
            .catch((error) => {
                if (error.response && error.response.data) {
                    window.alert(error.response.data.message);
                } else {
                    window.alert(error.message);
                }
            });
    } else {
        window.alert(
            "メールアドレス(ユーザーネーム)又はパスワードを入力してください。"
        );
    }
};
const UserLogout = async (navigate: NavigateFunction) => {
    try {
        await axios.post(`http://osk-196/api/logout`, null);
        navigate("/login");
    } catch (err) {
        console.log(err);
    }
};

const UserChange = (
    newpass: any
) => {
    axios
        .post(`http://osk-196/api/change `, newpass)
        .catch((error) => {
            if (error.response?.data.error.status == 400) {
                window.alert(error.response.data.error.message);
            }
        });
};

export {
    UserLogin,
    UserLogout,
    UserChange,
};
