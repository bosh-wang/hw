import * as dotenv from 'dotenv'
import { AppConfig } from './types/config'
import { serverOf, serverStart } from './server'

dotenv.config()

const server = serverOf()

const appConfig: AppConfig = {
  host: '0.0.0.0',
  port: 8888,
  mongoConnectionString: "mongodb://mongodb-server:27017/app"
}

serverStart(appConfig)(server)
  .then(() => {
    console.log(`Server listening on ${appConfig.host}:${appConfig.port}`)
  })
  .catch((err) => {
    console.error(err)
  })
