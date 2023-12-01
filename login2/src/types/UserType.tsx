export interface UserType {
   CurrentUser: {
       token: string | null,
       Session: string | null,
       UserInfo: {
         userid?: string;
         name?: string;
         email?: string;
       }
   }
   isFetching: boolean,
   isError: boolean,
}

export type currentUserType = UserType['CurrentUser'];